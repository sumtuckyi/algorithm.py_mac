import sys

n, m = map(int, input().split())
grid = []
coords = [] # 방문해야하는 지점의 좌표
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[False for _ in range(n)] for _ in range(n)]
res = 0 # 가능한 방법의 수

for i in range(n):
    grid.append(list(map(int, input().split())))
for i in range(m):
    x, y = map(int, input().split())
    coords.append((x - 1, y - 1))
visited[coords[0][0]][coords[0][1]] = True

def DFS(idx, x, y): # idx는 목적지 인덱스 처음엔 1에서 시작임
    global res
    if x == coords[idx][0] and y == coords[idx][1]:
        if idx == m - 1:
            res += 1
            return
        DFS(idx + 1, x, y)

    for i, j in delta:
        nx, ny = x + i, y + j
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue
        if visited[nx][ny] or grid[nx][ny] == 1:
            continue
        # if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and not visited[nx][ny] and grid[nx][ny] == 0:
        visited[nx][ny] = True
        DFS(idx, nx, ny)
        visited[nx][ny] = False

DFS(1, coords[0][0], coords[0][1])

print(res)
