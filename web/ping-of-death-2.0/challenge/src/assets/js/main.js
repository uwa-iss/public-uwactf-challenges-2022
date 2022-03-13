(function($) {
  $('#content').delay(1000).fadeIn('slow');
  $("#ping-to-death").click(function () {
    var ip = $("#ip-address").val();
    $("#result").text("Pinging to death " + ip + "! Please wait...")
    fetch(
      "/pingtodeath.php",
      {
        method: "post",
        headers : {
          "Content-Type" : "application/x-www-form-urlencoded"
        },
        body: "ip=" + ip
      }
    ).then(response => response.text()).then(function(data) {
      var result = $("#result")
      result.text(data);
      result.html(result.html().replace(/\n/g,'<br/>'));
    });
  });
})(jQuery);

particlesJS.load('particles-js', '/assets/js/particles.json', function() {})
