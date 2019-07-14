### input to program
argument1 is compared to '\x00' but we cannot pass null input to program from command line <br />
argument2 is compared to '\x20\x0a\x0d' that are ' \n\r' which too cannot be passed through command line <br />
these arguments are passed making another sol.c file and using execve <br />
execve takes full path of file and argument array and environ array <br />
code of sol.c is as follows 
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
int main(int argc,char**argv){
        char** new_argv[4];
        char**new_env[2];
        new_env[0]=NULL;
        new_argv[1]="\x00d";
        new_argv[2]="\x20\x0a\x0d";
        new_argv[3]=NULL;
        execve("/home/ringmaker/pwn/week/input",new_argv,new_env);
}
```

