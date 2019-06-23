program uses strcpy to copy characters starting leaving first four<br />
![](./pwn2-1.png)<br />
we run function with fairly large string with distinct 4 letter characters <br /> 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ' <br />
now pipe this output to file and give this file as input to program<br />
 and break point at comparison check the value of eax<br />
![](./pwn2-2.png)<br />
0x51 is hex of 'Q'<br />
so we print 64 characters then value eax is compared to that is '\x64\x63\x62\x61'<br />
that is 'dcba'<br />

