N = int(input())

d = [0]
p = [0]

for i in range(1, N + 1):
    days, pay = map(int, input().split())
    d.append(days)
    p.append(pay)

dp = p.copy()
for i in range(1, N + 1):
    next = i + d[i]
    if next > N + 1:
        dp[i] = 0
        continue
    for j in range(i + d[i], N + 1):
        if j <= N:
            dp[j] = max(dp[i] + p[j], dp[j])

print(max(dp))