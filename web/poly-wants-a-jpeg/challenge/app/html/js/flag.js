function show_flag(data) {
    $("#flag").text(data.value);
}

$(document).ready(() => {
    $.ajax({
        url : '/api/flag',
        type : 'GET',
        success : show_flag,
        error : error_callback
    });
});