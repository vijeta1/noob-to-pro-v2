<?php
if (isset($_GET['md5']))
{
	$md5=$_GET['md5'];
	$re='0'+md5($md5);
	if ($md5==$re){
		echo "<p style=color:white>JCTF{d351gn1ng_c7f_15_d1ff1cu17}";
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
<div >
<div style ='background-color:#00FFFF;width:40%'>
<pre>
if (isset($_GET['md5']))<br>
{<br>
<pre>$md5=$_GET['md5'];<br>
<pre>	$re='0'+md5($md5);<br>
<pre>	if ($md5==$re){<br>
<pre><pre>		echo $flag;<br>
<pre>    	}<br>
<pre>	else{<br>
<pre>        	echo "you are banned";<br>
<pre>	}<br>
}<br>

</div>
<form method="get">
	<input type="text" name="md5">
	<input type="submit" value="check">
</form>
<div>
</body>
</html>
