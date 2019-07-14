#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();
        int key=0;
        scanf("%d", &key);
        if(key==random){
                system("/bin/cat flag");
                return 0;
        }
        printf("Wrong.\n");
        return 0;
}
