<?php
if (isset($_GET['md5']))
{
	$md5=$_GET['md5'];
	$re='0'+md5($md5);
	if ($md5==$re){
		echo "access granted";
    	}
	else{
        	echo "you are banned";
	}
}


?>
<!DOCTYPE html>
<html>
<head>
</head>
<body>

<form method="get">
	<input type="text" name="md5">
	<input type="submit" value="check">
</body>
</html>
