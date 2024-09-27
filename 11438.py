import sys
import math
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
adj_list = [[] for _ in range(N + 1)]

# 1번 노드로부터의 거리 저장
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

depth = [0]*(N + 1)
MAX_DEPTH = int(math.log2(N)) + 1
# sparse table : 각 노드의 2^i번째 조상을 저장 -> parent[node][i]
parent = [[-1] * MAX_DEPTH for _ in range(N + 1)] # log(30만) <= 18, 즉 트리의 최대 깊이는 18


def dfs(node, par, d):
    depth[node] = d
    parent[node][0] = par  # node의 2^0 번째 부모 정보 저장
    for child in adj_list[node]:
        if child != par: # 양방향이므로 거슬러 올라가는 방향의 탐색은 걸러준다.
            dfs(child, node, d + 1)

dfs(1, -1, 0)

# sparse table 채우기
for i in range(1, MAX_DEPTH + 1): # 2^i번째 부모
    for j in range(1, N + 1): # 모든 노드를 탐색
        if parent[j][i - 1] != -1:  # 부모가 있는 경우에만
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(u, v):
    if depth[u] < depth[v]:  #u에 깊이가 더 깊은 노드를 할당(u의 깊이가 항상 v보다 크거나 같도록)
        u, v = v, u

    # 깊이 맞추기
    for i in range(MAX_DEPTH, -1, -1):
        if depth[u] - (1 << i) >= depth[v]: # 깊이를 v와 같거나 작을 때까지 줄이기
            u = parent[u][i]

    # 깊이를 맞췄는데 두 노드가 같아진다면 해당 노드가 공통 조상이므로 바로 반환
    if u == v:
        return u

    for i in range(MAX_DEPTH, -1, -1):
        if parent[u][i] != parent[v][i]: # 두 노드가 서로 다른 부모노드를 가리키는 한 계속 올라감
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]


M = int(input())
ans = []
for _ in range(M):
    u, v = map(int, input().split())
    ans.append(str(lca(u, v)))

print("\n".join(ans))