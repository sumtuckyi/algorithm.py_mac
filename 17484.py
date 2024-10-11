# 시작점과 도착점 고정,
# 위로는 이동 불가

# 최대 가치 출력 - 완전탐색.., dfs

def dfs(x, y, value, pre): # 현재 지점
    global min_value
    # 도착지점에 이르면 return
    if (x, y) in [(N-1, i) for i in range(M)]:
        min_value = min(min_value, value)
        return

    for idx, (dx, dy) in enumerate([(1, -1), (1, 0), (1, 1)]):
        if pre == idx:  # 이전에 선택한 방향과 같으면 패스
            continue
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny]:
            vis[nx][ny] = True
            dfs(nx, ny, value + grid[nx][ny], idx)
            vis[nx][ny] = False


N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
min_value = 1e10
vis = [[False for _ in range(M)] for _ in range(N)]

# 지구의 어느 지점에서든 출발 가능
for i in range(M): #i열 기준
    if i == 0:
        dfs(0, i, grid[0][i], 0)
        dfs(0, i, grid[0][i], 1)
    if i == M-1:
        dfs(0, i, grid[0][i], 1)
        dfs(0, i, grid[0][i], 2)
    else:
        for j in range(3):
            dfs(0, i, grid[0][i], j)
print(min_value)

