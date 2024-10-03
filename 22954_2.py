from collections import deque, defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]


def kruskal(edges, n):
    uf = UnionFind(n)
    mst = []
    for u, v, idx in sorted(edges, key=lambda x: x[2]):
        if uf.find(u) != uf.find(v):
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
    vertices = [start]
    edges = set()
    while q:
        cur = q.popleft()
        for nxt, idx in adj[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                q.append(nxt)
                vertices.append(nxt)
                edges.add(idx)
    return vertices, list(edges)


def split_mst(mst, N):
    adj = build_adj(mst)
    for i, (u, v, idx) in enumerate(mst):
        new_adj = adj.copy()
        new_adj[u] = [x for x in new_adj[u] if x[0] != v]
        new_adj[v] = [x for x in new_adj[v] if x[0] != u]

        vis = [False] * (N + 1)
        vertices_u, edges_u = bfs(u, new_adj, vis)
        vertices_v, edges_v = bfs(v, new_adj, vis)

        if len(vertices_u) != len(vertices_v):
            return vertices_u, edges_u, vertices_v, edges_v, idx
    return None


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) + (i + 1,) for i in range(M)]  # 간선 번호를 1부터 시작하도록 수정

if N < 3 or M == 0:
    print(-1)
else:
    mst = kruskal(edges, N)
    result = split_mst(mst, N)

    if result:
        vertices_u, edges_u, vertices_v, edges_v, removed_edge = result
        print(len(vertices_u), len(vertices_v))
        print(*sorted(vertices_u))
        print(*sorted(edges_u))
        print(*sorted(vertices_v))
        print(*sorted(edges_v))
    else:
        print(-1)