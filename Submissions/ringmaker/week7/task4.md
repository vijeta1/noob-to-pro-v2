## Cross site scripting

### Reflected XSS
credit card field is vulnerable to xss <br />

### DOM-Based XSS
![](./task4.png) <br />
checking JavaScript Source there is GoatRouter.js <br />
containing path 'start.mvc#test/'paramter passed is reflected back

### DOM-Based XSS
we call url `localhost:8000/WebGoat/start.mvc#test/<script>webgoat.customjs.phoneHome() <br />`
phone number in console

### Stored XSS
Just Comment `<script>webgoat.customjs.phoneHome()</script>`

