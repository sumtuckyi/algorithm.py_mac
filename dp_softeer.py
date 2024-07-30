# dp배열 2개를 이용하는 문제 - 나무 수확
import sys

n = int(input())
grid = []
dp = [[0] * n for _ in range(n)]
dp_double = [[0] * n for _ in range(n)]

# grid 입력받기
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# dp 배열 초기화
dp[0][0] = grid[0][0]
dp_double[0][0] = grid[0][0] * 2

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + grid[0][i]  # dp배열 첫 번째 행 초기화
    dp[i][0] = dp[i - 1][0] + grid[i][0]  # dp배열 첫 번째 열 초기화
    # dp_double배열의 첫 번째 행과 열을 초기화
    # 2배가 적용될 때, 경우의 수 고려 - 이미 앞선 경로에서 찬스를 쓴 경우와, 아직 쓰지 않았고 현재 지점에서 쓰는 경우를 비교
    dp_double[0][i] = max(dp_double[0][i - 1] + grid[0][i], dp[0][i - 1] + grid[0][i] * 2)
    dp_double[i][0] = max(dp_double[i - 1][0] + grid[i][0], dp[i - 1][0] + grid[i][0] * 2)

# dp배열 채우기
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # 찬스 사용 여부 * 위에서 오는지 왼쪽에서 오는지 여부 = 4가지
        dp_double[i][j] = max(
            dp_double[i - 1][j] + grid[i][j],  # 찬스 썼고, 위에서 오는 경우
            dp_double[i][j - 1] + grid[i][j],  # 찬스 썼고, 왼쪽에서 오는 경우
            dp[i - 1][j] + grid[i][j] * 2,  # 이번에 찬스를 쓰고, 위에서 오는 경우
            dp[i][j - 1] + grid[i][j] * 2  # 이번에 찬스를 쓰고, 왼쪽에서 오는 경우
        )

print(dp_double[n - 1][n - 1])




