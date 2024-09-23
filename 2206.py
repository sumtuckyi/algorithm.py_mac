# 최단 경로이므로 bfs 사용이 편할 듯..
# 문제는 1개의 벽을 부수는 경우를 시뮬레이션하는 것인데..
# 어찌됐든 그래프로 접근하는 거니까..

# 3차원 방문 배열, 3차원 bfs
from collections import deque


N, M = map(int, input().split())

grid = []
for i in range(N):
    row = list(map(int, input()))
    grid.append(row)


vis = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, 0, 1)])  # (x, y, z, dist) 에서 z는 벽을 부수고 도달했는지 그 여부
vis[0][0][0] = 1
while q:
    cur_x, cur_y, z, dist = q.popleft()

    if cur_x == N - 1 and cur_y == M - 1:  # 도착지점에 도착한 경우
        print(dist)
        exit()

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = cur_x + dx, cur_y + dy
        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
            # 벽이 아닌 경우
            if grid[nx][ny] == 0 and vis[nx][ny][z] == 0:
                q.append((nx, ny, z, dist + 1))
                vis[nx][ny][z] = dist + 1

            elif grid[nx][ny] == 1 and z == 0 and vis[nx][ny][1] == 0:
                q.append((nx, ny, 1, dist + 1))
                vis[nx][ny][1] = dist + 1

print(-1)





