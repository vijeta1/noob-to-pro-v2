<?php



ini_set("display_errors", 1);

$message = "";



if(isset($_REQUEST["login"]) & isset($_REQUEST["password"]))
{

    $login = $_REQUEST["login"];


    $password = $_REQUEST["password"];
    $xml = simplexml_load_file("passwords/list.xml");


    $result = $xml->xpath("/list/user[login='" . $login . "' and password='" . $password . "']");

    if($result)
    {

        $message =  "<p>Welcome <b>" . ucwords($result[0]->login) . "</b>, how are you today?</p><p>Your flag: <b>" . $result[0]->flag . "</b></p>";
 
    }

    else
    {

        $message = "<font color=\"red\">Invalid credentials!</font>";

    }


}

?>
<!DOCTYPE html>
<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


<script src="js/html5.js"></script>

<title>Welcome</title>

</head>

<body>

<header>

<h1>LOGIN PAGE</h1>


</header>


<div id="main">

    <h1> Login Form</h1>

    <p>Enter your  credentials.</p>

    <form action="<?php echo($_SERVER["SCRIPT_NAME"]);?>" method="GET">

        <p><label for="login">Login:</label><br />
        <input type="text" id="login" name="login" size="20" autocomplete="off" /></p>

        <p><label for="password">Password:</label><br />
        <input type="password" id="password" name="password" size="20" autocomplete="off" /></p>

        <button type="submit" name="form" value="submit">Login</button>

    </form>

    <br />
    <?php

    echo $message;

    ?>

</div>





</body>

</html>
