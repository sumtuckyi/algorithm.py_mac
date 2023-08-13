from collections import deque
def DFS(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if adj_m[v][i] == 1 and visited[i] == 0:
            DFS(i)


def BFS(v):
    visited[v] = 0
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if adj_m[v][i] == 1 and visited[i] == 1:
                visited[i] = 0
                queue.append(i)


N, M, V = map(int, input().split())
adj_m = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1
visited = [0]*(N+1)

DFS(V)
print()
BFS(V)
