we check source code using hopper<br/>
![](./pwn1.png)<br />
although it shows 0x0!=0x0 which comparison can never pass<br/>
but if a comparison can never pass it will not be included by compiler<br/>
actually it is comparisong b/w some variable not equal to zero <br/>
since program takes input using 'gets' and 'gets' doesnot takes amount of characters <br/>to input so we overwrite the variable by changing<br/> length of input string and it overwrites it for length>65 <br/>


