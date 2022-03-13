<html>
  <head>
    <title>My Secret Development Website</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/main.css" />
  </head>

  <body>
    <section>
      <div id="grid-item">
        <h1 style="color: rgb(0, 255, 34)">My Secret Development Website</h1>
      </div>

      <div id="grid-item">
        <p style="color: rgb(0, 255, 251)">Welcome to my secret development website!</p>
      </div>

      <div id="grid-item">
        <form action = "/topsecretconstruction/v1/index.php" method="get">
          <input type="hidden" name="page" value="flag.php" >
          <input type="submit" value="Get Flag">
        </form>
      </div>

      <div id="grid-item">
        <form action = "/topsecretconstruction/v1/index.php" method="get">
          <input type="hidden" name="page" value="dashboard.php" >
          <input type="submit" value="Open Dashboard">
        </form>
      </div>

      <div id="grid-item">
        <p>
        <?php
          if (isset($_GET['page'])) {
            include($_GET['page']);
          } else {
            include('flag.php');
          }
        ?>
        </p>
      </div>
    </section>

    <div id="particles-js"></div>
    <script src="/js/jquery.min.js"></script>
    <script src="/js/particles.min.js"></script>
    <script src="/js/main.js"></script>
  </body>
</html>
