# 원하는 만큼 간선을 삭제해 서로 다른 크기의 트리 2개로 분할
# 각 트리는 하나 이상의 정점을 가지고, 두 트리가 동일한 정점이나 간선을 공유해선 안 된다.
# 분할이 불가하면 -1을 출력
from collections import deque, defaultdict


# 분할 가능 여부부터 판단 - 어떻게?
# 처음부터 분할되어 있는 경우라면?
# N == 1 또는 2이면 분할 불가
# N >= 3 부터는 가능
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)  # 각 트리의 크기 저장

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]  # 트리 크기 갱신


N, M = map(int, input().split())


# adj_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
edges = []
adj_list = defaultdict(list)
for i in range(1, M + 1):
    a, b = map(int, input().split())
    adj_list[a].append((b, i))
    adj_list[b].append((a, i))
    edges.append((a, b, i)) # 가중치 대신 간선 번호 저장

if N < 3 or M == 0 :
    print(-1)
    exit()

def kruskal(edges, n):
    uf = UnionFind(n)
    mst = []

    for u, v, idx in edges:
        if uf.find(u) != uf.find(v): # 두 정점이 아직 연결되지 않았다면
            uf.union(u, v)
            mst.append((u, v, idx))

    return mst

def build_adj(mst):
    adj = defaultdict(list)
    for u, v, idx in mst:
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    return adj

def bfs(start, adj, vis):
    q = deque([start])
    vis[start] = True
    vertices = []
    edges = set()

    while q:
        cur = q.popleft()
        vertices.append(cur)
        for nxt, idx in adj[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                q.append(nxt)
                edges.add(idx)

    return vertices, edges


def split_mst(mst):
    edge = mst.popleft()
    u, v, idx = edge
    adj = build_adj(mst)
    vis = [False] * (N + 1)
    vertices_u, edges_u = bfs(u, adj, vis)
    vertices_v, edges_v = bfs(v, adj, vis)

    mst.append(edge)

    return vertices_u, edges_u, vertices_v, edges_v


# 처음부터 분할되어 있는 경우인지 판별

if M < N - 1: # mst를 이루는 간선의 수가 전체 노드의 수보다 2이상 작은 경우 : 입력이 애초에 하나의 그래프가 아닌 경우
    vis = [False] * (N + 1)
    components = []

    for i in range(1, N + 1):
        if vis[i]:
            continue
        v, e = bfs(i, build_adj(edges), vis)
        components.append((v, e))

    if len(components) != 2:  # 트리가 2개가 아니라면 = 3개 이상
        print(-1)
        exit()

    # 트리가 2개이면 -> 컴포넌트별 정점 수가 다른지 확인
    tree1, tree2 = components
    v1, e1 = tree1
    v2, e2 = tree2
    if len(v1) == len(v2):
        print(-1)
        exit()

    print(len(v1), len(v2))
    print(*v1)
    print(*e1)
    print(*v2)
    print(*e2)

else: # mst가 구성되는 경우라면
    mst = deque(kruskal(edges, N))  # mst 생성
    for _ in range(N - 1): # mst를 이루는 간선의 개수
        vertices_u, edges_u, vertices_v, edges_v = split_mst(mst)
        # print(vertices_u, edges_u, vertices_v, edges_v)
        if len(vertices_u) != N - len(vertices_u): # 두 트리의 크기가 다르면
            print(len(vertices_u), N - len(vertices_u))
            print(*vertices_u)
            print(*edges_u)
            print(*vertices_v)
            print(*edges_v)
            break
