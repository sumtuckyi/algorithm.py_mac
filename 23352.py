# 가장 긴 경로의 시작 + 끝, 최대 경로의 길이가 같은 경우가 여러 개라면 숫자의 합이 큰 것을 출력
# 시작과 끝이 동일할 수 있다. 0이 아닌 한 이동 가능
# bfs로 접근
from collections import deque
N, M = map(int, input().split())

grid = []
for _ in range(N):
    row = list(input())
    grid.append(row)

max_t = 0
def bfs(x, y): # 탐색의 최초 시작점
    global max_t
    q = deque()
    q.append((x, y, 0)) # x, y, 이동시간

    while q:
        cur_x, cur_y, t = q.popleft()
        max_t = max(t, max_t)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = cur_x + dx
            ny = cur_y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if vis[nx][ny] or grid[nx][ny] == 'W':
                    continue
                vis[nx][ny] = True
                q.append((nx, ny, t + 1))


for i in range(N):
    for j in range(M):
        if grid[i][j] == 'W':
            continue
        vis = [[False]*(M) for _ in range(N)]
        vis[i][j] = True
        bfs(i, j)

print(max_t)