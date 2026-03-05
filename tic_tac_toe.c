#include <stdio.h>

char board[9] = {'1','2','3','4','5','6','7','8','9'};

void display() {
    printf("\n");
    printf(" %c | %c | %c\n",board[0],board[1],board[2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",board[3],board[4],board[5]);
    printf("---+---+---\n");
    printf(" %c | %c | %c\n",board[6],board[7],board[8]);
}

int checkWin() {

    int win[8][3] = {
        {0,1,2},{3,4,5},{6,7,8},
        {0,3,6},{1,4,7},{2,5,8},
        {0,4,8},{2,4,6}
    };

    for(int i=0;i<8;i++){
        if(board[win[i][0]] == board[win[i][1]] &&
           board[win[i][1]] == board[win[i][2]])
           return 1;
    }

    return 0;
}

int main() {

    int player = 1, pos;
    char mark;

    for(int i=0;i<9;i++) {

        display();

        player = (i%2==0) ? 1 : 2;
        mark = (player==1) ? 'X' : 'O';

        printf("Player %d enter position: ",player);
        scanf("%d",&pos);

        board[pos-1] = mark;

        if(checkWin()) {
            display();
            printf("Player %d wins\n",player);
            return 0;
        }
    }

    display();
    printf("Game Draw\n");

    return 0;
}
