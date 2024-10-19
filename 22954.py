# 원하는 만큼 간선을 삭제해 서로 다른 크기의 트리 2개로 분할
# 각 트리는 하나 이상의 정점을 가지고, 두 트리가 동일한 정점이나 간선을 공유해선 안 된다.
# 분할이 불가하면 -1을 출력
from collections import deque, defaultdict
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# 분할 가능 여부부터 판단 - 어떻게?
# 처음부터 분할되어 있는 경우라면?
# N == 1 또는 2이면 분할 불가
# N >= 3 부터는 가능
N, M = map(int, input().split()) # 정점의 개수, 간선의 개수

adj_list = [[] for _ in range(N + 1)]
# 정점 번호는 1부터 시작
for i in range(1, M+1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append((n2, i))  # 간선번호도 함께 저장
    adj_list[n2].append((n1, i))


def count_graph(): # 최초에 몇 개의 그래프가 존재하는지 세기
    vis = [False]*(N + 1)
    graphs = []

    def dfs(v, i, graph):
        vis[v] = True
        graph.append((v, i))
        for n, idx in adj_list[v]:
            if vis[n]:
                continue
            dfs(n, idx, graph)

    for i in range(1, N+1):
        if vis[i]:
            continue
        graph = []
        dfs(i, 0, graph)
        graphs.append(graph)

    return graphs


def prim_mst(start):
    mst_edges = []
    vis = [False]*(N + 1)
    pq = [(start, -1)]  # 현재 정점, 간선 번호
    last_node, last_edge = None, None

    while pq:
        node, edge = heapq.heappop(pq)

        if vis[node]:
            continue
        vis[node] = True
        if edge != -1:  # 시작 간선이 아닌 경우
            mst_edges.append(edge)
            last_node = node # 가장 마지막으로 추가된 노드를 추적
            last_edge = edge # 가장 마지막으로 추가된 간선을 추적

        for nxt, nxt_edge in adj_list[node]:
            if not vis[nxt]:
                heapq.heappush(pq, (nxt, nxt_edge))

    return mst_edges, last_node, last_edge

if N == 1 or N == 2:  # 주어진 정점의 개수가 2개 이하면 불가능
    print(-1)
    exit()

graphs = count_graph()
if len(graphs) >= 3:
    print(-1)
    exit()

if len(graphs) == 2: # 처음부터 두 개의 그래프이고
    if len(graphs[0]) != len(graphs[1]): # 둘의 크기가 다르다면
        print(len(graphs[0]), len(graphs[1])) # 각 그래프 정점의 수
        print(*[x[0] for x in graphs[0]])
        print(*[x[1] for x in graphs[0] if x[1] != 0])
        print(*[x[0] for x in graphs[1]])
        print(*[x[1] for x in graphs[1] if x[1] != 0])

    else: # 크기가 같다면
        print(-1)
        exit()

if len(graphs) == 1:  # 처음부터 하나의 그래프라면 : 이때 노드의 개수는 3개 이상이므로 한 개만 떼어내어 그래프를 만드는 경우 두 그래프의 크기가 같아질 수 없다.
    mst, last_node, last_edge = prim_mst(1)
    print(N - 1, 1) # 각 그래프의 크기
    print(*[i for i in range(1, N + 1) if i != last_node])
    print(*[i for i in mst if i != last_edge])
    print(last_node)
    # print(last_edge)
