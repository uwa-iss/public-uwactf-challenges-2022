function upload_success(data) {
    var path = data.value.path;
    var msg = data.value.msg;
    console.log("Successful upload");
    $.notifyBar({
        cssClass: "success", 
        html: "<p>"+msg+"</p><br /><p>Click <a href='"+path+"'>here</a> to see!",
        delay : 7000,
        animationSpeed : "normal"
    });
}

$("input#submit").on('click', () => {
    console.log("submit");
    var from = $("input#name").val();
    var upload = $("input[type=file]").prop('files')[0];
    var formData = new FormData();
    formData.append('file', upload)
        
    $.ajax({
        url : '/api/jpegs/submit?name='+from,
        type : 'POST',
        data : formData,
        contentType : false,
        cache : false,
        processData : false,
        success : upload_success,
        error : error_callback
    });
});