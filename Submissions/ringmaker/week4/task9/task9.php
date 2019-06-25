<?php
$target_URL="task9.xml";
$html = new DOMDocument();
@$html->loadHTMLFile($target_URL);
$login = simplexml_load_file($target_URL);
if(isset($_POST['user'])){
	$user=$_POST['user'];
	$pass=$_POST['pass'];
	$isuser=0;
	$result=$login->xpath("/company/employee[user='$user']");
	foreach($result as $employ) {
		if(employ->pass==$pass){
			echo "hello {$employ->firstname}<br />";
			$isuser=1;
		}
    	}
	if(!$isuser){
		echo("username or password incorrect");
	}
	exit();
}

?>
<!DOCTYPE html>
<html>
<head>
</head>
<body>

<form method="post">
	<input type="text" name="user">
	<input type="text" name="pass">
	<input type="submit" value="check">
</body>
</html>
