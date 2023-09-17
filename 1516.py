'''
N개의 건물에 대해 각 건물이 완성되기까지 걸리는 최소시간을 N줄로 출력
pre = [] 각 건물의 사전건물의 번호를 이차원 배열로 저장
dp[N] = max(dp[N], dp[i]+t[N])
여기서 i는 사전에 지어져야하는 건물의 번호이다.
for j in range(1, N+1):
    if j번 건물은 사전에 지어져야 하는 건물이 없는 경우:
        dp[j] = [N]
    else: 사전에 지어져야 하는 건물이 있는 경우
        for m in pre[N]:
            dp[j] = max(dp[N], dp[m] + t[N])
for k in range(1, N+1):
    print(dp[k])
'''

N = int(input())
t = [0 for _ in range(N+1)]
pre = [[] for _ in range(N+1)]
for i in range(1, N+1):
    t[i], *b = map(int, input().split())
    pre[i].extend(b)

dp = [0]*(N+1)
for j in range(1, N+1):
    if len(pre[j]) == 1:
        dp[j] = t[j]

for j in range(1, N+1):
    for m in pre[j]:
        if m != -1:
            dp[j] = max(dp[j], dp[m] + t[j])

print(t)
print(pre)
print(dp)
for k in range(1, N+1):
    print(dp[k])