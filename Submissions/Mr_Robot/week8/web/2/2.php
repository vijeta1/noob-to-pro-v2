
<!DOCTYPE html>
<?php
if (isset($_GET['login']))
{   if(strcmp($_GET['login'],"India")===0)
	{
		echo "loggedin?? so what!! ";
    	}
	else{
        	echo "no chance";
	}
}
?>

<html>
<head>
</head>
<body>

<div id="main">

    <h1> Enter the username</h1>

    
    <form  method="GET">

        <p><label for="login">Login:</label><br />
        <input type="text"  name="login" size="20" autocomplete="off" /></p>


        <button type="submit" name="form" value="submit">Login</button>

    </form>

    <br />

<h1>Do you know anything about 2011 world cup </h1>

<h2>That time Indian Squad had some great players in it   </h2>

<p><h2>Virat Kohli</h2>
Passionate. No word describes Virat Kohli better. His passion for cricket has made him one of the best batsmen in the world across formats, and has also helped him grow into a ruthless captain. It's also passion that defines Kohli's emotional, effervescent and at times firecracker character. Virat Kohli does not hold back and that remains his strength. 

</p>

<p><h2>Yuvraj Singh</h2>

Yuvraj Singh is an Indian international cricketer, who plays all forms of the game. An all-rounder who bats left-handed in the middle order and bowls slow left-arm orthodox, Yuvraj is the son of former Indian fast bowler and Punjabi actor Yograj Singh.

</p>

<p><h2>Gautam gambhir</h2>

Gautam Gambhir is an Indian cricketer, who played all formats of the game. He is a left-handed opening batsman 
<!--JCTF{true_star}-->
who plays domestic cricket for Delhi, and captained Kolkata Knight Riders in the Indian Premier League. He made his One Day International debut against Bangladesh in 2003, and played his first Test the following year against Australia.

</p>


<p><h2>M.S Dhoni</h2>
Mahendra Singh Dhoni is an Indian international cricketer who captained the Indian national team in limited-overs formats from 2007 to 2016 and in Test cricket from 2008 to 2014. An attacking right-handed middle-order batsman and wicket-keeper, he is widely regarded as one of the greatest finishers in limited-overs cricket.
</p>

<p><h2>Sachin Tendulkar</h2>
Sachin Ramesh Tendulkar is a former Indian international cricketer and a former captain of the Indian national team, regarded as one of the greatest batsmen of all time. He is the highest run scorer of all time in International cricket.
</p>

<p><h2>Virender Sehwag</h2>
Virender Sehwag is a former Indian cricketer. Widely regarded as one of the most destructive batsmen of all time, Sehwag played as an aggressive right-handed opening batsman and also bowled part-time right-arm off-spin. He played his first One Day International in 1999 and joined the Indian test side in 2001.
</p>


</div>
</body>
