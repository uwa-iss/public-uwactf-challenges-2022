function load_jpegs(data) {
    jpegs = data.value;

    jpegs.forEach((jpeg) => {
        $('section').append('<div id="grid-item"><a href="'+ jpeg.path +'"><h3 style="color: rgb(0, 255, 255);">Image uploaded from '+ encodeURI(jpeg.from) + '</h3></a>');
    });
}

$(document).ready(() => {
    $.ajax({
        url : '/api/jpegs/list',
        type : 'GET',
        success : load_jpegs,
        error : error_callback
    });
});