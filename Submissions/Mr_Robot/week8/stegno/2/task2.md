## Statement 


you again !! it's not obvious this time. have you ever wonder how beautiful it is that the red, green , blue   (# RGB #) etc colours  together gives the rainbow ,well we don't need seven ,adding 3 of them can give what we need to pass.
your rainbow is at (1,1).

![](duck1.png)

## Difficulty:medium

## Solution

this time it says not obvious so  using  "ash" as passphrase in stegosuite won't give anything. as statement mention {RGB} 

extract the rgb value of image and add them.
x,y={1,1} as statement says.
for extracting...

```
from PIL import Image

im = Image.open('duck1.png') 
pix = im.load()
print im.size  
print pix[1,1]

```

rgb=[(252, 253, 252)]
sum=757
so passphrase is 757
using that we get the flag .

## flag 
flag:JCTF{it_is_a_flag}
