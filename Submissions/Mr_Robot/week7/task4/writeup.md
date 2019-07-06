## Objective

Complete XSS

## Solution

i)Cross Site Scripting

2.seeing the cookies they are same.

7.we need to find out field susceptible to XSS.

first four field show red indication on pasting <script>alert('ss')</script>
on credit card no. we did't get error.

![](xss7.png)

10.as it says we need to see the source code . seeing the source of goatrouter.js

![]xss10r.png

we see test just like lesson.lesson has route start.mvc#lesson/
so test will have route start.mvc#test/

![]xss10.png

11. as it says use the previous route we will use it and it says via url.
so type 
http://localhost:8080/WebGoat/start.mvc#test/<script>webgoat.customjs.phoneHome()<%2Fscript>
in new tab with web console open .

![]xss11r.png

we got the no. in the console

![]xss11.png

ii)Cross Site Scripting (stored)

3.run the scrpit in the comment and as it says watch the browser console.

<script>webgoat.customjs.phoneHome()</script>

![](xsss3r.png)

copying that response we get success.













