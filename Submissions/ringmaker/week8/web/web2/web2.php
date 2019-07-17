<?php
if($_POST['password']=='heda'&&$_POST['user']=='admin'&&$_POST['csrf']=='98737263'){
	echo '<p style=color:white;>JCTF{c5rf_15_cr4p}</p>';
}
?>
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h2>try login as admin <br>password is 4 digit alphabetic lowercase and in decreasing order of hex value</h2>
<form method='post'>
<label>username</label>
<input type='text' name='user'>
<label>password</label>
<input type='text' name='password'>
<input type='hidden' value='98737263' name='csrf'>
<input type='submit' value='check'>
</form>
</body>
</html>
