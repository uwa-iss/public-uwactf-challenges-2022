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

$(document).ready(() => {
    $('section').delay(500).fadeIn(500);
});