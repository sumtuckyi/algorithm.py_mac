import sys
from collections import deque

N = int(sys.stdin.readline())
cur = [0, 0]  # 아기 상어의 위치(탐색 기준점)
how_big = 2
time = 0
sea = [] # 맵
q = deque()
for i in range(N):
    row = list(map(int, sys.stdin.readline()))
    sea.append(row)
    for j in range(N):
        if row[j] == 9:
            cur[0], cur[1] = i, j

def can_eat_or_not(from, to, how_big):  # 타겟 물고기에 도달 가능한지 판단
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q.append([from[0], from[1]])
    while q:
        from_x, from_y = q.popleft()   # 현재 아기 상어의 위치
        to_x, to_y = to[0], to[1]  # 먹으려는 물고기의 위치
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= from_x + dx < N and 0 <= from_y + dy < N:
                if visited[from_x + dx][from_y + dy]:
                    continue
                if[from_x + dx][from_y + dy] <= how_big:
                    visited[from_x + dx][from_y + dy] = 1
                    q.append([from_x + dx, from_y + dy])
    if visited[to_x][to_y]: # 도달 가능하면
        return True
    else:
        return False


def search_for_prey(cur_x, cur_y):  # 먹을 수 있는 물고기 찾기 - 거리, y좌표, x좌표 순으로 고려
    min_d, min_y, min_x = float('inf'), float('inf'), float('inf')
    for i in range(N):
        for j in range(N):
            if sea[i][j] >= how_big or sea[i][j] == 0: # 먹을 수 없는 물고기거나 빈 칸이면 패스
                continue
            if abs(cur_x - i) + abs(cur_y - j) < min_d: # 더 가까운 물고기를 찾았다면 갱신
                min_d = abs(cur_x - i) + abs(cur_y - j)
                min_y, min_x = i, j
            elif abs(cur_x - i) + abs(cur_y - j) == min_d: # 거리가 동일한 물고기를 찾았다면
                if min_y > i: # y 좌표를 확인해서 더 아래라면
                    min_y = i # 갱신하고 다음 칸 탐색
                    min_x = j
                    continue
                elif min_y == i: # 같다면
                    if min_x > j: # 더 왼쪽에 있는 경우에만 갱신
                        min_x = j
                        min_y = i
    return min_y, min_x

# search_for_prey의 리턴값이 float('inf')이면 더 이상 먹을 수 있는 물고기가 없는 것
while True:
    target = search_for_prey(cur[0], cur[1])
    if target[0] == float('inf'):
        break
    if can_eat_or_not(cur, target, how_big): # 도달 가능하면
        sea[target[0]][target[1]] = 9 # 아기 상어가 이동
        sea[cur[0]][cur[1]] = 0
        how_big += 1 # 상어의 크기 증가
        time += 1 # 이동 시간 소요
    else: # 도달 가능하지 않다면 다음 타겟을 찾아야함










