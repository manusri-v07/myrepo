#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    int captcha;
    int userInput;

    srand(time(0));

    captcha = rand() % 9000 + 1000;   // generates 4 digit captcha

    printf("CAPTCHA: %d\n", captcha);

    printf("Enter CAPTCHA: ");
    scanf("%d", &userInput);

    if(userInput == captcha)
        printf("Verification Successful\n");
    else
        printf("Verification Failed\n");

    return 0;
}
