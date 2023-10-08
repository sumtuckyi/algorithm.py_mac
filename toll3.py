import heapq


def dijkstar(s, adj_m):
    pq = []
    distance[s][0] = 0
    heapq.heappush(pq, (0, s, 0))

    for node, cost in adj_m[s]:
        distance[node][1] = cost

    while pq:
        cur_cost, cur_city, cnt_c = heapq.heappop(pq)
        tof = False
        for i in range(cnt_c + 1):
            if distance[cur_city][i] < cur_cost:
                tof = True
                break

        if cnt_c == N - 1 or tof:
            continue
        for node, cost in adj_m[cur_city]:
            new_cost = cur_cost + cost
            if distance[node][cnt_c + 1] < new_cost:
                continue
            distance[node][cnt_c + 1] = new_cost
            heapq.heappush(pq, (new_cost, node, cnt_c + 1))


N, M, K = map(int, input().split())
S, D = map(int, input().split())
adj_li = [[] for _ in range(N + 1)]
distance = [[float('inf') for _ in range(N)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
pp = []
for i in range(M):
    a, b, c = map(int, input().split())
    adj_li[a].append((b, c))
    adj_li[b].append((a, c))
for i in range(K):
    pp.append(int(input()))

dijkstar(S, adj_li)
min_v = 1e9
for i in range(N):
    if min_v > distance[D][i]:
        min_v = distance[D][i]
        limit = i
print(distance[D][limit])

toll = 0
for i in range(K):
    min_v = 1e9
    toll += pp[i]
    for c in range(1, limit + 1):
        if distance[D][c] > distance[D][c - 1]:
            continue
        if min_v > distance[D][c] + c * toll:
            min_v = distance[D][c] + c * toll
    print(min_v)