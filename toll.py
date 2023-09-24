# from collections import deque
#
# direction = [(0,-1), (-1,0), (0,1), (1,0)]
#
#
# def BFS():
#     q = deque([(0,0)])
#     visited[0][0] = 1
#     while q:
#         check = q.popleft()
#         for k in range(4):
#             ny = check[0] + direction[k][0]
#             nx = check[1] + direction[k][1]
#             if ( 0 <= ny < N ) and ( 0 <= nx < N ):
#                 fuel = 1
#                 if matrix[ny][nx] > matrix[check[0]][check[1]]:
#                     fuel += matrix[ny][nx] - matrix[check[0]][check[1]]
#                 if visited[ny][nx] > (visited[check[0]][check[1]] + fuel):
#                     visited[ny][nx] = visited[check[0]][check[1]] + fuel
#                     q.append((ny,nx))
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[10**6]*N for _ in range(N)]
#     BFS()
#     print(f"#{tc} {visited[N-1][N-1]-1}")
# 도시번호는 1부터 N까지
import heapq


def dijkstra(s):
    pq = []
    distance[s][0] = 0
    heapq.heappush(pq, (0, s, 0))  # 누적 통행료, 시작도시, 거쳐온 도시의 수

    while pq:
        cc, now, visited = heapq.heappop(pq)
        # 최적화 조건
        if visited == N-1:  # 해당 도시를 제외한 모든 도시를 다 거쳐 온 것이라면 ?
            continue
        for i in range(visited+1):  # 거쳐온 도시의 수가 같거나 작은 경로에 대해서
            if distance[now][i] < cc:
                continue

        # 현재 도시 기준으로 인접도시 확인
        for next in range(1, N+1):
            if adj_m[now][next] == 0:
                continue
            # 인접한 노드이면
            total_cost = cc + adj_m[now][next]
            if distance[next][visited+1] > total_cost:
                distance[next][visited+1] = total_cost
                heapq.heappush(pq, (total_cost, next, visited + 1))


N, M, K = map(int, input().split())
A, B = map(int, input().split())
adj_m = [[0 for _ in range(N+1)] for _ in range(N+1)]
distance = [[float('inf') for _ in range(N)] for _ in range(N+1)]
pp = [0]
for _ in range(M):
    f, t, c = map(int, input().split())
    adj_m[f][t] = adj_m[t][f] = c

for _ in range(K):  # 통행료 인상폭 저장
    pp.append(int(input()))

dijkstra(A)
print(min(distance[B]))  # 방문한 도시수, 도착도시
toll = 0
for k in range(1, K+1):
    min_v = 1e9
    toll += pp[k]
    for j in range(1, N):
        if min_v > distance[B][j] + j * toll:
            min_v = distance[B][j] + j * toll
    print(min_v)
    print(distance[B])  # 방문한 도시수, 도착도시



# for i in range(K+1):  # K번 인상되므로 0부터 K번째 해까지 구함
#     print(dijkstra(A, pp[i]))
#     distance = [float('inf') for _ in range(N + 1)]


