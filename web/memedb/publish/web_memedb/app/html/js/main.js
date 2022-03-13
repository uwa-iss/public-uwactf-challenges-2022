$("#slideshow > div:gt(0)").hide();

function update_slideshow(data) {
    $("#slideshow").empty();
    
    var memes = data.value;
    memes.forEach((meme) => {
        $("#slideshow").append("<div><h3>" + encodeURI(meme.name) + "</h3><img id='slideshow-img' src=" + encodeURI(meme.url) +"></img></div>")
    });

    if (memes.length === 1) {
        $("#slideshow").append("<div><h3>" + encodeURI(memes[0].name) + "</h3><img id='slideshow-img' src=" + encodeURI(memes[0].url) +"></img></div>")
    }

    $("#slideshow > div:gt(0)").hide();
}

function error_callback(xhr, status, error) {
    console.log("YEET");
    var data = JSON.parse(xhr.responseText);
    $("#error-query").text(data.value);
    $("#error-query").fadeIn(1000).delay(5000).fadeOut(1000);
}

function url_success(data) {
    $("#submit-meme-response").text(data.value);
    $("#submit-meme-response").fadeIn(1000).delay(5000).fadeOut(1000);
}

function search_memes(query_str) {
    var q = ""
    if (query_str.length >= 0) {
        q = "?q="+query_str;
    }

    $.ajax({
        url : "/api/search" + q,
        success : update_slideshow,
        error: error_callback
    });
}

setInterval(function() { 
    $('#slideshow > div:first')
    .fadeOut(1000)
    .next()
    .fadeIn(1000)
    .end()
    .appendTo('#slideshow');
}, 5000);

$(document).ready(() => {
    $('#content').delay(500).fadeIn(500);
    $('#slideshow').delay(1000).fadeIn(500)
    search_memes("");
});

$("#search-meme").click(()=>{
    var query_meme = $("#query-meme").val();
    console.log(query_meme);
    search_memes(query_meme);
});

$("#submit-meme").click(() => {
    var url = $("#meme-url").val();

    $.ajax({
        url : "/api/submit", 
        type : "POST",
        data : JSON.stringify({"url": url}),
        dataType: "json",
        contentType: "application/json",
        success : url_success,
        error : error_callback
    });
});

particlesJS.load('particles-franku', '/js/franku.json', () => {});
particlesJS.load('particles-doge', '/js/doge.json', () => {});
particlesJS.load('particles-pepe', '/js/pepe.json', () => {});
particlesJS.load('particles-hacker', '/js/hacker.json', () => {});