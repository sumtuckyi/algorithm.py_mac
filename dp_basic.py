# from collections import deque
# n = int(input())  # 맵의 크기
# s = list(map(int,input().split()))  # 각 칸에서 얻는 점수
# dp = [0 for _ in range(n+2)]  # 시작점과 도착점 포함
#
# # dp리스트 채우기
# dp[2] = s[1]
# dp[7] = s[6]
# q = deque([2, 7])
# while q:
#     cur = q.popleft()
#     if cur + 2 <= n:
#         q.append(cur+2)
#     if cur + 7 <= n:
#         q.append(cur+7)
#     if cur < 7:  # 6번째칸 이하인 경우
#         dp[cur] = dp[cur-2] + s[cur-1]
#     else:
#         if dp[cur-7] == 0:  # 현재칸의 7칸 전의 칸이 2와 7의 조합으로 도달할 수 없는 경우(즉, 현재칸은 무조건 직전에 두 칸 점프로 도착하게 된 것)
#             dp[cur] = dp[cur-2] + s[cur-1]
#         else:
#             dp[cur] = max(dp[cur-2] + s[cur-1], dp[cur-7] + s[cur-1])
#
#
# print(max(dp))

n = int(input())  # 맵의 크기
s = list(map(int,input().split()))  # 각 칸에서 얻는 점수
dp = [0 for _ in range(n+2)]  # 시작점과 도착점 포함

if n == 1:
    print(0)
    exit()
elif n == 2:
    if s[1] > 0:
        print(s[1])
    else:
        print(0)
    exit()

# dp리스트 채우기
dp[2] = s[1]
for i in range(3, n+1):
    if i < 7:  # 6번째칸 이하인 경우
        if dp[i-2] == 0:
            continue
        dp[i] = dp[i-2] + s[i-1]
    else:
        if dp[i-7] == 0:  # 현재칸의 7칸 전의 칸이 2와 7의 조합으로 도달할 수 없는 경우(즉, 현재칸은 무조건 직전에 두 칸 점프로 도착하게 된 것)
            dp[i] = dp[i-2] + s[i-1]
        else:
            dp[i] = max(dp[i-2] + s[i-1], dp[i-7] + s[i-1])
print(max(dp))
