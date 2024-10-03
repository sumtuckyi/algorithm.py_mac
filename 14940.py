from collections import deque

N, M = map(int, input().split())

grid = []
goal = None
for i in range(N):
    row = list(map(int, input().split()))
    if goal is None:
        for j, num in enumerate(row):
            if num == 2:
                goal = (i, j)
    grid.append(row)
vis = [[-1 for _ in range(M)] for _ in range(N)]
vis[goal[0]][goal[1]] = 0
def bfs():
    q = deque()
    q.append(goal)

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if vis[nx][ny] == -1:  # 아직 방문하지 않았으면
                    if grid[nx][ny] == 1:
                        vis[nx][ny] = vis[x][y] + 1
                        q.append((nx, ny))

bfs()
#원래부터 갈 수 없는 곳은 0을 출력
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            vis[i][j] = 0
for row in vis:
    print(' '.join(map(str, row)))