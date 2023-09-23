# 코딩던전
# 주어진 골드로 입장 가능한 던전의 번호를 오름차순으로 출력
from collections import deque


def bfs():
    visited = [0]*(N+1)
    visited[0] = 1
    while q:
        now, k = q.popleft()
        for i in range(1, N+1):
            if visited[i]:
                continue
            if adj_m[now][i] != 0:
                if k-adj_m[now][i] >= 0:
                    q.append((i, k-adj_m[now][i]))
                    visited[i] = 1
                    possible.append(i)



N, M, K = map(int, input().split())  # 노드의 개수, 간선의 개수, 골드의 양
adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
q = deque([(0, K)])  # (시작 노드, 남은 골드)
possible = []
for _ in range(M):
    a, b, g = map(int, input().split())
    adj_m[a][b] = adj_m[b][a] = g
bfs()
possible.sort()
print(*possible)