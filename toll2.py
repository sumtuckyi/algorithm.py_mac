# 도시번호는 1부터 시작
# 다익스트라 함수 처음부터 다시 구현하기 - 여러 알고리즘으로 해보기
import heapq
N, M, K = map(int, input().split())
A, B = map(int, input().split())
# adj_li = [[] for _ in range(N+1)]
adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]
pp = [0]
for _ in range(M):
    f, t, c = map(int, input().split())
    # adj_li[f].append([t, c])
    adj_m[f][t] = adj_m[t][f] = c

for _ in range(K):
    pp.append(int(input()))

print(adj_m)
def dijkstra(s, p):  # 시작점과 비용에 더해줄 값을 인자로 전달
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0
    # 통행료 업데이트
    for i in range(1, N+1):
        for j in range(1, N+1):
            if adj_m[i][j] == 0:
                continue
            adj_m[i][j] += p
    print(p, adj_m)
    while pq:
        d, now = heapq.heappop(pq)
        if distance[now] < d:
            continue

        for i in range(1, N+1):  # node의 형식은 [node_n, w]
            if not adj_m[now][i]:
                continue
            can_node = i
            cost = adj_m[now][i]

            n_cost = d + cost
            if n_cost >= distance[can_node]:
                continue
            distance[can_node] = n_cost
            heapq.heappush(pq, (n_cost, can_node))

    return distance[B]


for i in range(K+1):  # K번 인상되므로 0부터 K번째 해까지 구함
    print(dijkstra(A, pp[i]))

    distance = [float('inf') for _ in range(N + 1)]