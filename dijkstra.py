import heapq
n, e = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float('inf') for _ in range(n)]
visited = [False]*n
pq = []

for _ in range(e):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

def dijkstra():
    distance[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        # 이미 방문한 노드라면 패스???
        if visited[cur_node]:
            continue
        visited[cur_node] = True

        for next_node, edge_cost in graph[cur_node]:
            total_cost = cur_cost + edge_cost
            if distance[next_node] > total_cost:
                distance[next_node] = total_cost
                heapq.heappush(pq, (total_cost, next_node))


dijkstra()
# 목표한 지점(n-1)과 연결되어 있지 않았다면 distance[n-1]은 여전히 초기화 값일 것임
if distance[n-1] == float('inf'):
    print('impossible')
else:
    print(distance[n-1])

