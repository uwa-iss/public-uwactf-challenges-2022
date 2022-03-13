<?php
function check_for_bad_chars($ip) {
  $filter = str_split("();'\",<>!#%^&*_ |\\?\n\r~[]");

  foreach ($filter as $bad_char) {
    if (strpos($ip, $bad_char) !== false) {
      return true;
    }
  }
  return false;
}

if (isset($_POST) and !empty($_POST["ip"])) {
  $ip = $_POST["ip"];

  if (check_for_bad_chars($ip) === true) {
    echo "\nBugger off hacker! 🤬";
    return;
  } 
  system("ping -c 10 $ip");
  echo "\nYou need to pay some money to do more pings!";
} else {
  echo "lol you can't even properly send me an IP address lol";
}
?>
