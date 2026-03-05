#include <stdio.h>
#include <string.h>

int main() {

    char input[100];

    printf("Hello! Ask me something:\n");

    fgets(input, sizeof(input), stdin);

    if(strstr(input, "name"))
        printf("My name is AI System.\n");
    else if(strstr(input, "how are you"))
        printf("I am functioning properly.\n");
    else
        printf("Interesting question!\n");

    printf("\nJudge: Was that Human or Machine?\n");

    return 0;
}
