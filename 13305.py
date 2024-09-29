N = int(input())
dist = list(map(int, input().split()))
p = list(map(int, input().split()))

cost = 0
cur = 0
while cur < N - 1:
    if cur == N - 2:
        cost += p[-2] * dist[-1]
        break
    if p[cur] >= p[cur + 1]:
        cost += p[cur] * dist[cur]
        cur += 1
    else:
        nxt = cur + 2
        while nxt < N - 1 and p[nxt] > p[cur]:
            nxt += 1
        cost += sum(dist[cur:nxt])*p[cur]
        cur = nxt  # 주유할 도시 갱신

print(cost)