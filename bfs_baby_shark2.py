import sys
from collections import deque
import heapq

N = int(sys.stdin.readline())
how_big = 2
time = cnt = 0
sea = []  # 맵
start = []  # 상어의 최초 위치
q = deque()
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    sea.append(row)
    for j in range(N):
        if row[j] == 9:  # 상어의 위치 파악
            start = [i, j]

# visited = [[-1 for _ in range(N)] for _ in range(N)]
# eat_or_not = [[0 for _ in range(N)] for _ in range(N)]  # 먹을 수 있는지 여부
# 현재 상어의 위치 기준으로 먹이 탐색
def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 0  # 시작점 거리 초기화
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if sea[next_x][next_y] > how_big or visited[next_x][next_y] != -1: # 이동불가한 칸이거나 이미 방문한 칸이면 패스
                    continue
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1 # 방문체크 및 거리 저장
                if 0 < sea[next_x][next_y] < how_big:  # 먹을 수 있는 물고기가 있는 칸이면
                    eat_or_not[next_x][next_y] = 1  # 체크
                q.append([next_x, next_y])


def any_prey():
    # 먹을 수 있는 물고기가 있는지 탐색
    min_dist = float('inf')
    min_x = min_y = float('inf')
    for i in range(N):
        for j in range(N):
            if eat_or_not[i][j] == 1: # 먹을 수 있는 물고기가 있는 칸이면 거리 계산
                if min_dist > visited[i][j]:
                    min_dist = visited[i][j]
                    min_x, min_y = i, j
                elif min_dist == visited[i][j]:
                    if min_x != i:  # 행이 다르다면
                        if min_x > i: # 더 위쪽 행의 좌표를 최솟값으로
                            min_x = i
                            min_y = j
                            continue
                    else:  # 행이 같다면, 열을 비교하여 갱신
                        min_y = min(min_y, j)

    return min_x, min_y, min_dist


# 최솟값이 갱신되지 않았다면 먹을 수 있는 물고기가 없는 것임
while True:
    shark_x, shark_y = start[0], start[1]
    # print('현재 위치:', shark_x, shark_y)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    eat_or_not = [[0 for _ in range(N)] for _ in range(N)]  # 먹을 수 있는지 여부
    bfs(shark_x, shark_y)
    min_x, min_y, min_dist = any_prey()
    if min_x == float('inf'):  # 먹을 수 있는 먹이가 없다면
        break
    else:  # 먹을 수 있는 먹이가 있다면
        # print('먹을 수 있는 먹이가 있군')
        # 해당 위치로 이동해서 먹기
        sea[min_x][min_y] = 0
        sea[shark_x][shark_y] = 0
        # print('먹은 후 맵의 상황: ', sea)
        # 이동 시간 더해주기
        time += min_dist
        # print('소요시간: ', time)
        # 먹은 물고기 수 카운트
        cnt += 1
        # print('지금까지 먹은 물고기 수: ', cnt)
        # 상어 크기 갱신
        if how_big == cnt:
            how_big += 1
            cnt = 0
        # print('현재 크기: ', how_big)
        # 상어 위치 갱신
        start[0], start[1] = min_x, min_y
        # print('새로운 위치: ', start[0], start[1])

print(time)



