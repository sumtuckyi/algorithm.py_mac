N, M = map(int, input().split())  # 노드와 간선의 수
adj_m = [[0]*(N+1) for _ in range(N+1)]  # NxN크기 인접배열
adj_l = [[] for _ in range(N+1)] # N개의 요소를 가지는 인접 리스트
visited = [0] * (N+1)
for _ in range(M):  # 인접배열 채우기
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1
    adj_l[x].append(y)

def DFS(v):  # v는 시작 노드
    for i in range(1, N+1):
        if i in adj_l[v] and not visited[i]:
            DFS(i)
    visited[v] = 1
    print(v, end=' ')

DFS(1)
