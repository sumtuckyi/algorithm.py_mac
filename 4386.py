# 별의 개수는 최대 100개
# 별의 좌표가 주어진다.
# 별을 연결하는 비용은 별 사이의 거리이다.
# 미리 별 사이의 거리(비용)를 계산 -> 1만 개의 간선 정보
# N개의 별이 있으면 최소 N-1개의 간선이 필요하다.
# 오차는 소숫점 둘째자리까지 허용
# MST 만들기 - 프림 알고리즘

import math, heapq

N = int(input())

stars = []
for _ in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))

# 거리 저장하기 - NC2개
dist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N): # 0부터 N-1까지
    for j in range(N): # 0부터 N-1까지
        if i == j:
            continue
        if dist[j][i] != 0:
            dist[i][j] = dist[j][i]
        d = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        dist[i][j] = round(d, 2)

def prim(start):
    mst = []
    visited = [False] * N
    min_heap = [(start, 0)] # 가중치, 정점
    total = 0

    while min_heap: # 모든 간선을 검토할 때까지
        w, u = heapq.heappop(min_heap)

        if visited[u]: # 이미 트리에 포함되어 있으면 패스
            continue

        visited[u] = True
        mst.append((w, u))
        total += w

        for nxt in range(N): # 자신을 제외한 N-1개의 노드와 모두 연결 가능함
            if visited[nxt]:
                continue
            heapq.heappush(min_heap, (dist[u][nxt], nxt))
    return total


print(prim(0))
