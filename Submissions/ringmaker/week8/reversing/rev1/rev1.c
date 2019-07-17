#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>

int main(int argc, char* argv[]){
	printf("Welcome to CTF\n");
	printf("------------------------------------------------------------------\n");
	if(argc != 3) return 0;
	if(strcmp(argv[1],"\x00")){
		printf("Wrong INPUT");
		return 0;
	}
	if(strcmp(argv[2],"\x20\x0a\x0d")){
		printf("WRONG INPUT");
		return 0;
	}
	// here's your flag
	system("/bin/cat flag");
	return 0;
}

