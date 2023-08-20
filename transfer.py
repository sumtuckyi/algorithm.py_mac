# def bfs():
#     q = [(sy, sx, 0, 0)]  # 출발점과 현재 버스 번호, 누적 환승횟수를 큐에 삽입
#     print(q)
#     # visited[sy][sx] = 1  # 방문했음을 표시
#     while q:
#         cy, cx, cb, cnt = q.pop(0)  # 탐색 시작점, 타고 온 버스 번호, 환승횟수
#         print(cy, cx, cb, cnt)
#         visited[cy][cx] = 1  # 해당 정류장을 방문했음을 표시
#         buses = lines[cy][cx]  # 현 지점에서 탈 수 있는 버스 종류
#         # print(cy, cx, '에서 탈 수 있는 버스', buses)
#         for i in range(1, len(buses)):  # 탈 수 있는 버스 각각을 타고 가는 경우
#             q.append((cy, cx, buses[i], cnt))
#
#         if len(buses) > 1:  # 버스가 지나는 곳인 경우에만
#
#             # for i in range(1, len(buses)):  # 순차적으로 타고 가봄
#             #     cb = buses[i]  # 현재 탄 버스의 번호
#             #     print('bus number', cb)
#             for a, b in d:
#                 if 1 <= cx + a <= m and 1 <= cy + b <= n:  # 지도의 범위 내에 있고
#                     if not visited[cy + b][cx + a] and len(lines[cy + b][cx + a]) >= 2:  # 아직 방문하지 않았고 버스가 다니는 지점이라면
#                         if (cy + b, cx + a) == (ey, ex):  # 해당 지점이 도착점인 경우
#                             print(cy, cx, cb, cnt)
#                             return cnt
#                         elif cb in lines[cy + b][cx + a]:  # 현재 버스가 해당 지점을 지나가는 경우
#                             # print(cb, '가', cy + b, cx + a, '를 지나감')
#                             q.append((cy + b, cx + a, cb, 0))
#
#                         elif cb not in lines[cy + b][cx + a] and len(lines[cy + b][cx + a]) >= 2:  # 해당 지점을 지나가지 않지만 다른 버스는 다니는 경우
#                             # print(cb, '가', cy + b, cx + a, '를 안 지나가니', cy, cx, '에서 환승해야함')
#                             for j in range(1, len(lines[cy + b][cx + a])):
#                                 q.append((cy + b, cx + a, lines[cy + b][cx + a][j], cnt + 1))  # 환승해야함
#                                 # print(cb, (cy + b, cx + a, lines[cy + b][cx + a][j], cnt + 1))
#
#     return 1

from collections import defaultdict
def bfs(v):
    visited = [0] * (k + 1)
    q= [v]  # 출발점
    visited[v] = 1
    while q:
        cn = q.pop(0)
        for i in range(1, k+1):
            if adj_m[cn][i] == 1 and not visited[i]:
                if i in arrival_node:
                    return visited[cn]
                q.append(i)
                visited[i] = visited[cn] + 1


m, n = map(int, input().split())  # 맵의 크기 (열의 크기, 행의 크기)
k = int(input())  # 버스의 수
line_dict = defaultdict(list)
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            line_dict[b].append((y, x))
sx, sy, ex, ey = map(int, input().split())  # 열과 행 순서임

start_node = []  # 시작점으로 가능한 노드
arrival_node = []  # 도착점으로 가능한 노드
# arrival_node의 길이가 2이상이면 즉 환승역이면 최소환승횟수를 구할 때 최소 거리에 1을 더할 필요가 없음
for i in range(1, k+1): # 도착 노드 구하기
    if (ey, ex) in line_dict[i]:
        arrival_node.append(i)
for j in range(1, k+1):
    if (sy, sx) in line_dict[j]:
        start_node.append(j)
# 인접 배열 만들기
adj_m = [[0] * (k+1) for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(1, k+1):
        if i == j:
            continue
        if set(line_dict[i]) & set(line_dict[j]):  # 두 노드가 연결되어 있으면
            adj_m[i][j] = adj_m[j][i] = 1
result = []
for i in start_node:
    result.append(bfs(i))
ans = min(result) if len(arrival_node) > 1 else min(result)+1
print(ans)


'''
from collections import deque

m, n = map(int, input().split())
k = int(input())

# 교차점의 리스트
bus_routes = [set() for _ in range(k)]
for i in range(k):
    _, x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2: # 수직 노선
        for y in range(min(y1, y2), max(y1, y2) + 1):
            bus_routes[i].add((x1, y))
    else: # 수평 노선
        for x in range(min(x1, x2), max(x1, x2) + 1):
            bus_routes[i].add((x, y1))

sx, sy, dx, dy = map(int, input().split())
start = (sx, sy)
end = (dx, dy)

# BFS
def bfs():
    visited = [False] * k
    queue = deque([(start, 0)])
    while queue:
        pos, trans = queue.popleft()
        if pos == end:
            return trans

        # 현재 위치에서 가능한 모든 버스 찾기
        for bus_num, route in enumerate(bus_routes):
            if pos in route and not visited[bus_num]:
                visited[bus_num] = True
                # 해당 버스의 다른 교차점을 큐에 추가
                for next_pos in route:
                    queue.append((next_pos, trans + 1))

    return -1

print(bfs())
print(bus_routes)
'''
