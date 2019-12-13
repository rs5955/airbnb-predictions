<!DOCTYPE html>
<html>
  <head>
    <title>Airbnb Search</title>
    <link rel="stylesheet" type="text/css" href="design.css">
    <link rel="icon" href="logo.jpg" type="image/jpg">
  </head>
  <body>
    <h1>Airbnb Questionnaire</h1>
    <i>answer the following questions to get your accommodation options!</i><br>
    <form action="index.php" method="post">
    <br>What is the zipcode of your hometown (where you grew up living)?
    <br><input type="number" name="hometown">
    <br>
    <br>What is the zipcode of your current town?<br>
    <input type="number" name="current"><br>
    <p><input type="submit" value="submit">
    <p><input type="reset">
    </form>
    <?php
    $hometown = $_POST['hometown'];
    $current = $_POST['current'];
    $marital = $_POST['marital'];
    $education = $_POST['education'];
    $gender = $_POST['gender'];
    $age = $_POST['age'];
    $fp = fopen("responses.txt","a") or die("cant open");

    fwrite($fp,$hometown.",".$current."\n");
    fclose($fp);
    ?>
  </body>
</html>
