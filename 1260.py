from collections import deque

N, M, V = map(int, input().split()) # 정점의 개수(1부터 N), 간선 개수, 시작정점

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t = map(int, input().split())
    adj_list[f].append(t)
    adj_list[t].append(f)
for li in adj_list:
    li.sort()

vis1 = [False]*(N + 1)
vis2 = [False]*(N + 1)
dfs_arr = []
bfs_arr = []


def dfs(v):
    dfs_arr.append(v)
    vis1[v] = True
    for n in adj_list[v]:
        if vis1[n]:
            continue
        dfs(n)


def bfs(v):
    q = deque()
    q.append(v)
    vis2[v] = True
    while q:
        cur = q.popleft()
        bfs_arr.append(cur)
        for nxt in adj_list[cur]:
            if vis2[nxt]:
                continue
            vis2[nxt] = True
            q.append(nxt)

dfs(V)
bfs(V)


print(' '.join([str(x) for x in dfs_arr]))
print(' '.join([str(x) for x in bfs_arr]))