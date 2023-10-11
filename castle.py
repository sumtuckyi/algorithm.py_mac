import sys
from copy import deepcopy

N, M, D = map(int, sys.stdin.readline().split())
enemies = []

visited = [0] * M
res = 0
# 보드의 상태를 입력받으며 적의 위치 좌표를 저장
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(board)

def simulator():
    global res
    min_d = float('inf')
    min_y = M
    min_coord = [100, 100]
    cnt = 0  # 사살한 적의 수
    # 적의 위치 좌표
    enemies_copy = deepcopy(enemies)
    while True:
        # 각 궁수의 위치에서 사살 가능한 적이 있는지 판단(하나의 턴)
        num_of_e = 0 # 보드에 남은 적의 수
        print(visited)
        for archer in range(M):
            if visited[archer]:
                for x in range(N):
                    for y in range(M):# 현재 보드에 있는 모든 적에 대해
                        if board[x][y] == 0:
                            continue
                        # D 이내이면서 거리가 가장 짧은 적 찾기
                        dist = abs(archer-y) + abs(N-x)
                        if dist > D:  # 사정거리 밖이면 패스
                            continue
                        if min_d >= dist and min_y > y:  # 가장 가까운 적 갱신
                            min_d = dist
                            min_y = y
                            min_coord = [x, y]
                # 모든 가능한 위치를 다 돌았다면
                if min_coord[0] == 100:  # 범위 내에 사살 가능한 적이 없는 경우
                    continue
                target_x, target_y = min_coord[0], min_coord[1]
                board[target_x][target_y] = 0
                cnt += 1
        print('한 턴 종료', cnt)
        # 적의 위치 좌표 이동(아래로 한 칸씩)
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1 and i < N-1: # 맨 아래줄이 아니면
                    board[i+1][j] = 1
                    num_of_e += 1
                    board[i][j] = 0
                elif board[i][j] == 1 and i == N-1: # 맨 아래줄이면
                    board[i][j] = 0
        print('한 턴 종료후 보드에 남은 적의 수', num_of_e)
        if num_of_e == 0:
            break
    res = max(res, cnt) # 최대 사살 가능한 적의 수 갱신


# 궁수 3명의 위치를 선택(완전탐색)
def set_archer(level, limit):
    if level == 3: # 3명의 위치가 정해지면
        simulator()
        return
    for i in range(limit + 1, M): # M개의 열 중에 선택
        if visited[i]:
            continue
        visited[i] = 1
        set_archer(level + 1, i)
        visited[i] = 0


set_archer(0, -1)
print(res)