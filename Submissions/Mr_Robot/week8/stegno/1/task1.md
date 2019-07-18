## Statement 

Are you still a child?? .try the obvious.

Difficulty : medium

![](duck1.jpg)

## Solution

the task is of stegno with a jpg file.

download the file .

using steghide

```
steghide extract -sf duck1.jpg

```
it will ask for passphrase .as the problem statement says try the obvious and the image is of a pokemon named psyduck.

trying ""ash"" the  main character of pokemon.

we get file named r.txt.
```
cat r. txt

```
it says md of "21be35e821c0cc413736a78274ef4464" . using  any online md5 decoder 

we get the flag. 

## flag
 JCTF{the flag}
