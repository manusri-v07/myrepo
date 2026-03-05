#include <stdio.h>

#define MAX 10

int dls(int graph[MAX][MAX], int node, int goal, int limit, int n) {
    if (node == goal)
        return 1;

    if (limit <= 0)
        return 0;

    for (int i = 0; i < n; i++) {
        if (graph[node][i] == 1) {
            if (dls(graph, i, goal, limit - 1, n))
                return 1;
        }
    }

    return 0;
}

int main() {
    int n = 4;

    int graph[MAX][MAX] = {
        {0,1,1,0},
        {1,0,0,1},
        {1,0,0,1},
        {0,1,1,0}
    };

    if (dls(graph, 0, 3, 2, n))
        printf("Goal Found\n");
    else
        printf("Goal Not Found\n");

    return 0;
}
