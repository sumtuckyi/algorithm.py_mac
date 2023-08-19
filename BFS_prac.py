def match(V):
    q = []
    q.append(V)
    visited[V] = 1
    while q:
        cn = q.pop(0)
        for i in range(1, N+1):
            if adj_m[cn][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)


N = int(input())
T = int(input())
adj_m = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0]*(N+1)
for i in range(T):
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1
coco = int(input())
partner = int(input())
match(coco)
result = 'NO' if visited[partner] == 0 else 'YES'
print(result)
