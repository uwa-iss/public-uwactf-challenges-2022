function error_callback(xhr, status, error) {
    var data = JSON.parse(xhr.responseText);
    $.notifyBar({
        cssClass: "error", html: "<p>" + data.value + "</p>",
        delay : 5000,
        animationSpeed : "normal"
    });
    // var data = JSON.parse(xhr.responseText);
    // $("#error-query").text(data.value);
    // $("#error-query").fadeIn(1000).delay(5000).fadeOut(1000);
}

function url_success(data) {
    console.log("Success!")
}

function load_the_parrots() {
    var total_parrots = 6;
    var total_columns = 25;
    var total_rows = 25;
    var parrot_index = 0;

    for (var x=1; x < total_rows + 1; x++) {
        for (var y=1; y < total_columns; y++) {
            parrot_index = Math.floor(Math.random() * total_parrots) + 1;
            $('#parrot-bg').append($("<img />",{
                id : 'parrot-img',
                style : "grid-row: " + x + + "; grid-column: " + y,
                src : "/images/background/parrot" + parrot_index + ".gif"
            }).delay(1000 + 5*(x*total_columns + y)).fadeTo(1000, 2*(x/total_rows-0.5)**2));
        }
    }
}

$(document).ready(() => {
    let getParams = new URLSearchParams(window.location.search);
    if (!getParams.has("noparrots")) {load_the_parrots();}
    $('section').delay(500).fadeIn(500);
});