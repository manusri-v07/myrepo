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

void iddfs(int graph[MAX][MAX], int start, int goal, int maxDepth, int n) {

    for (int i = 0; i <= maxDepth; i++) {
        if (dls(graph, start, goal, i, n)) {
            printf("Goal found at depth %d\n", i);
            return;
        }
    }

    printf("Goal not found\n");
}

int main() {

    int n = 4;

    int graph[MAX][MAX] = {
        {0,1,1,0},
        {1,0,0,1},
        {1,0,0,1},
        {0,1,1,0}
    };

    iddfs(graph, 0, 3, 3, n);

    return 0;
}
