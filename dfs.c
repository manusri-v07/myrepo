x#include <stdio.h>

#define MAX 10

int visited[MAX];

void dfs(int graph[MAX][MAX], int n, int v) {
    int i;

    visited[v] = 1;
    printf("%d ", v);

    for (i = 0; i < n; i++) {
        if (graph[v][i] == 1 && !visited[i]) {
            dfs(graph, n, i);
        }
    }
}

int main() {
    int n = 4;

    int graph[MAX][MAX] = {
        {0,1,1,0},
        {1,0,0,1},
        {1,0,0,1},
        {0,1,1,0}
    };

    dfs(graph, n, 0);

    return 0;
}
