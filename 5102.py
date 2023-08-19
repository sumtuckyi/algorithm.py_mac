T = int(input())

def bfs(s, g):
    q = []
    visited[s] = 1
    q.append(s)
    while q:
        cn = q.pop(0)
        if cn == g:
            return visited[cn]-1
        for i in range(1, V+1):
            if adj_m[cn][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[cn] + 1
    return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_m = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        x, y = map(int, input().split())
        adj_m[x][y] = adj_m[y][x] = 1
    S, G = map(int, input().split())
    result = bfs(S, G)
    print(f'#{tc} {result}')