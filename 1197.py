import heapq

V, E = map(int, input().split())


adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))


def prim(start):
    mst = []
    visited = [False] * (V + 1)  # 1번부터 V번
    min_heap = [(0, start)]  # 가중치, 정점
    total = 0  # 가중치의 합

    while min_heap:  # 모든 간선을 검토할 때까지
        w, u = heapq.heappop(min_heap)

        if visited[u]:  # 이미 트리에 포함되어 있으면 패스
            continue

        visited[u] = True
        mst.append((w, u))
        total += w

        for nxt, cost in adj_list[u]:  # 자신을 제외한 N-1개의 노드와 모두 연결 가능함
            if visited[nxt]:
                continue
            heapq.heappush(min_heap, (cost, nxt))
    return total

print(prim(1))