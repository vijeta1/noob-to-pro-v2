## Objective

Complete Request Forgerie

## Solution

i) Cross-Site Request Forgeries

3.click on submit query .
it says success:false
now seeing the url we see csrf=false
changing it to true

![](csrf3r.png)

it says success :true
got flag:22018

![](csrf3.png)

4.as it says request using extenal source. we will use burp  . first turn on the intercept and click on submit review.
seeing the request it contains a Validreq ,stars,reviewtext.we will use the cookie(jsessionid) and do the same request,

![](csrf4r.png)

the response is lessoncompleted=true

![](csrf4.png)

7.seeing the hint it says see content type.open burp suit and intercept the request we see content-type :json
so to post the required content we will do similar to previous one. and in our request we will use content-type :plain-text
and will name and rest like the image below.

![](csrf7r.png)

seeing the response it contains the flag.

![](csrf7.png)

8.seeing the hints it says First create a new account with csrf-username
so i have user =gourav81
now i will make account using csrf-gourav81.
after that go to same task then click solved.
we succed.

![](csrf8.png)

ii)Server-Side Request Forgery

2.as the task says to change the url we will do that exactly. using burpsuit intercept the request .
we see it have a url .
so replace tom with jerry (as we need jerry)

![](ssrf2r.png)

forward the request.

![](ssrf2.png)

3.seeing the hint it says add http://
we will do exactly same as previous .we need ifconfig.pro so add url in request to http://ifconfig.pro
![](ssrf3r.png)

forward the request.

![](ssrf3.png)



















