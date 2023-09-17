from collections import deque
from sys import stdin
N = int(stdin.readline())
t = [0 for _ in range(N+1)]
pre = [[] for _ in range(N+1)]
d = [0]*(N+1)  # 각 노드의 진입차수 저장
q = deque()
adj_lst = [[] for _ in range(N+1)]
dp = [0]*(N+1)
# 진입차수와 진출차수 저장
for i in range(1, N+1):
    t[i], *b = map(int, stdin.readline().split())
    pre[i].extend(b)
    if len(pre[i]) == 1: # 진입차수가 0인 노드이면
        q.append(i)
        dp[i] = t[i]
    else:
        d[i] = len(pre[i])-1  # 진입차수 저장
        for j in pre[i]:
            if j != -1:
                adj_lst[j].append(i)  # i번 건물이 지어져야 j번이 지어질 수 있음

# dp배열 채우기
while q:
    cur = q.popleft()
    if adj_lst[cur]:
        for i in list(adj_lst[cur]):
            d[i] -= 1
            dp[i] = max(dp[i], dp[cur] + t[i])
            if d[i] == 0:
                q.append(i)
for i in range(1, N+1):
    print(dp[i])