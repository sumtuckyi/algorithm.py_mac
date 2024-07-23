import sys

# 최대 4쌍 선택(2*4=8그루)
# 격자는 최소 4칸에서 최대 16칸

# n = 2이면 모든 나무 선택
# n = 3이면 (0, 1), (1, 0), (1, 2), (2, 1)위치를 제외한 5곳 중 최솟값을 제외한 모든 수
# n = 4이면 완전탐색
n = int(input())
total_trees = 0
grid = []


def in_grid(a, b, n):
    return 0 <= a < n and 0 <= b < n


def dfs(grid, visited, n, pairs, current_sum):
    if pairs == 4:  # 최대 4쌍을 선택했으면
        max_sum[0] = max(max_sum[0], current_sum)
        return

    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            for dx, dy in [(0, 1), (1, 0)]:  # 오른쪽, 아래쪽 인접한 칸만 확인
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny, n) and not visited[nx][ny]:
                    # 현재 칸과 인접한 칸을 선택
                    visited[x][y] = visited[nx][ny] = True
                    dfs(grid, visited, n, pairs + 1, current_sum + grid[x][y] + grid[nx][ny])
                    visited[x][y] = visited[nx][ny] = False


for _ in range(n):
    row = list(map(int, input().split()))
    total_trees += sum(row)
    grid.append(row)

if n == 2:
    print(total_trees)
    exit()

elif n == 3:
    min_val = 20
    for i in range(n):
        for j in range(n):
            if (i, j) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
                continue
            if grid[i][j] < min_val:
                min_val = grid[i][j]
    print(total_trees - min_val)
    exit()

else:
    max_sum = [0] # global 정수 변수 대신 가변 객체인 리스트 사용
    visited = [[False] * n for _ in range(n)]
    dfs(grid, visited, n, 0, 0)
    print(max_sum[0])

