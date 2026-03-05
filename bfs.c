#include <stdio.h>

#define MAX 10

int queue[MAX], front = -1, rear = -1;
int visited[MAX];

void enqueue(int v) {
    if (rear == MAX - 1)
        return;
    if (front == -1)
        front = 0;
    queue[++rear] = v;
}

int dequeue() {
    if (front == -1)
        return -1;
    int item = queue[front];
    if (front == rear)
        front = rear = -1;
    else
        front++;
    return item;
}

void bfs(int graph[MAX][MAX], int n, int start) {
    int i;
    enqueue(start);
    visited[start] = 1;

    while (front != -1) {
        int v = dequeue();
        printf("%d ", v);

        for (i = 0; i < n; i++) {
            if (graph[v][i] == 1 && !visited[i]) {
                enqueue(i);
                visited[i] = 1;
            }
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

    bfs(graph, n, 0);

    return 0;
}
