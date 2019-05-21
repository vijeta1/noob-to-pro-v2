# Week-1 : Lab Setup and basics

**( Timeline : 22<sup>th</sup> May'19 - 26<sup>th</sup> May'19 )**
 
1. Bascis of SSH and SSH tunnelling,  SCP , SFTP.

2. Shell scripting , Automating as many tasks as possible.

3. Proxy setting up using different environment variables , like 
	* all_proxy
	* http_proxy
	* https_proxy
	* Setting in **/etc/environment** file etc


4. Set up **2 VMs** ,
	1. Vagrant [EpicTreasure](https://github.com/ctfhacker/EpicTreasure) and change according to your needs ( like it has 8gb RAM and 4 cores assigned for the virtual box , change it accordingly to suit your system ).
	2. The 2nd being [Flare-VM](https://github.com/fireeye/flare-vm) windows virtual machine.

These two would contain moslty all the tools you would ever need for either Windows reversing or Linux reversing/pwning or basic maleware analysis.


|#| Task		| Points	|	Format To Submit	|
|--| ------------- 	| -------------	|	-------------------		|
|1| SSH Reverse tunnelling ( one liner script )<sup>1</sup>  | 50  |	C	|
|2| SSH script ( one liner script ) to unning remote commands from local host  | 50 |  C |
|3| One liner to copy a _folder_ to a directory named **week-1** on remote server/vagrant VM  | 50  |	C	|
|4| SFTP connection to the remote server/ vagrant VM  | 50  |	S	|
|5| Proxy Setting using export command  | 50  |		C	|
|6| Setting up vagrant VM  | 100  |		G/V	|
|7| Setting up vagrant Flare-VM  | 100  |		G/V	|
|8| **BONUS** : Write a script for task 1-5	| 200	| C	|
|| **TOTAL** 	| **650**	|

1 : Show the output of `lsof` to show the port is opened and which program is running on this port.


Index	|	|
--------|-------|
C	| Code	|
S	| Screenshot	|
G/V	| Gif/Video	|


### enjoy hacking :)
### try harder
