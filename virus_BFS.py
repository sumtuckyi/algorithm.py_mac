from collections import deque
from copy import deepcopy
N, M = map(int, input().split()) # 세로, 가로
board = [list(map(int, input().split())) for _ in range(N)]
coords = []
cases = []
q = deque()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 맵을 돌면서 0의 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            coords.append((i, j))
        if board[i][j] == 2:  # 바이러스의 위치를 큐에 삽입
            q.append((i, j))


def back_tracking(depth, lst):
    global cases
    # 종료 조건
    if depth == 3:
        cases.append(lst.copy())  # 결과 리스트에 현재 경우를 추가
        return
    for i in range(len(coords)):
        if coords[i] in lst:  # 중복 걸러내기
            continue
        lst.append(coords[i])
        back_tracking(depth + 1, lst)
        lst.pop()


back_tracking(0, [])
max_v = 0


print(q)
for i in range(len(cases)):  # 벽이 세워질 수 있는 각 경우에 대해
    cnt = 0
    temp = deepcopy(board)
    for j in range(3):
        temp[cases[i][j][0]][cases[i][j][1]] = 1
    while q:
        x, y = q.pop()
        # print(x, y)
        for k in range(len(d)):  # 상하좌우 탐색
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < N and 0 <= dy < M:
                if temp[dx][dy] == 0: # 감염되지 않은 영역이라면
                    temp[dx][dy] = 2  # 감염시키고
                    q.appendleft((dx, dy))  # 감염된 지점의 좌표를 큐에 추가
                    # print('감염시킨 뒤 출력', temp)

    temp_c = deepcopy(temp)

    for l in range(N):
        for m in range(M):
            if temp_c[l][m] == 0:
                cnt += 1

    if max_v < cnt:
        max_v = cnt

