from collections import deque
from sys import stdin

T = int(stdin.readline())
for _ in range(1, T + 1):
    N, K = map(int, stdin.readline().split())
    t = list(map(int, stdin.readline().split()))
    adj_list = [[] for _ in range(N+1)]
    cnt = [0 for _ in range(N+1)] # 진입차수 저장
    for i in range(1, K+1):
        a, b = map(int, stdin.readline().split())
        adj_list[a].append(b)
        cnt[b] += 1
    target = int(stdin.readline())

    q = deque()
    dp = [0 for _ in range(N+1)]
    # 진입차수가 0인 노드 저장
    for i in range(1, N+1):
        if cnt[i] == 0:
            q.append(i)
            dp[i] = t[i-1]

    while q:
        cur = q.popleft()
        if adj_list[cur]:
            for i in list(adj_list[cur]):
                cnt[i] -= 1
                dp[i] = max(dp[i], dp[cur] + t[i-1])
                if cnt[i] == 0:
                    q.append(i)

    print(dp[target])