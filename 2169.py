# # 시작점과 도착점 고정,
# # 위로는 이동 불가
import sys
sys.setrecursionlimit(10**9)


def dfs(x, y, d):
    if x == N-1 and y == M-1:
        return grid[x][y]

    if dp[x][y][d] != -1e10:  # 이미 계산된 값이 있다면
        return dp[x][y][d]

    vis[x][y] = True
    res = -1e10
    for i, (dx, dy) in enumerate([(0, 1), (0, -1), (1, 0)]): # 오른쪽, 왼쪽, 아래
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny]:
            res = max(res, dfs(nx, ny, i))

    vis[x][y] = False
    dp[x][y][d] = grid[x][y] + res
    return dp[x][y][d]


N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

vis = [[False for _ in range(M)] for _ in range(N)]
dp = [[[-1e10 for _ in range(3)] for _ in range(M)] for _ in range(N)]
answer = dfs(0, 0, 0)
# print(dp)
print(answer)