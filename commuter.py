def move(r):
    q = []
    q.append(r)
    visited[r] = 1
    while q:
        cn = q.pop(0)
        for i in range(1, N+1):
            if adj_m[cn][i] == 1 and visited[i] == 0:
                visited[i] = visited[cn] + 1
                q.append(i)


N, M = map(int, input().split())
adj_m = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1
R, K = map(int, input().split())
move(R)
for i in visited:
    if 0 <= i-1 <= K:
        cnt += 1
print(cnt)