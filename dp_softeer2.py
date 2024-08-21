import sys

N = int(input())  # 작업장의 개수
# 조립라인은 단 두 개 뿐.
# 조립라인에 따라 작업 시간이 다를 수 있으며 이동 시에는 일정 시간이 걸린다.
arr_a = []  # 작업장별 작업시간
arr_b = []
move_a = []  # move_a[i]는 i+1번째 a작업장에서 다음 b작업장까지 이동하는데 걸리는 시간
move_b = []
dp = [[0] * (N + 1) for _ in range(2)]

for _ in range(N - 1):
    a, b, a_to_b, b_to_a = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)
    move_a.append(a_to_b)
    move_b.append(b_to_a)
an, bn = map(int, input().split())
arr_a.append(an)
arr_b.append(bn)

# 예를 들어 N = 3이면 총 3번의 작업을 거쳐야 조립이 완료된다. 단 단계별 조립 라인은 바뀔 수 있다.
# dp배열 채우기 - 0행은 a, 1행은 b
dp[0][1] = arr_a[0]
dp[1][1] = arr_b[0]
for i in range(2, N + 1):  # i는 작업장의 번호(1부터 N까지 있음)
    # i번째 작업장으로 a조립라인을 선택한 경우
    dp[0][i] = min(arr_a[i - 1] + dp[0][i - 1], arr_a[i - 1] + move_b[i - 2] + dp[1][i - 1])
    # i번째 작업장으로 b조립라인을 선택한 경우
    dp[1][i] = min(arr_b[i - 1] + dp[1][i - 1], arr_b[i - 1] + move_a[i - 2] + dp[0][i - 1])

# 자동차 한 대의 가장 빠른 조립 시간을 도출하라.
print(min(dp[0][N], dp[1][N]))