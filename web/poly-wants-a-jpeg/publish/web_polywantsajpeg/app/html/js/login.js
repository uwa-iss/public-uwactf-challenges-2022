function login_success(data) {
    $.notifyBar({
        cssClass : "success",
        html : "<p>"+data.value.msg+"</p>",
        delay : 3000,
        animationSpeed : "normal"
    });

    window.location.href = data.value.redirect;
}

$("input#submit").on("click", () => {
    var username = $("input#username").val();
    var password = $("input#password").val();

    $.ajax({
        url : '/api/login',
        type : 'POST',
        data : JSON.stringify({"username" : username, "password" : password}),
        dataType : "json",
        contentType : "application/json",
        success : login_success,
        error : error_callback
    });
});