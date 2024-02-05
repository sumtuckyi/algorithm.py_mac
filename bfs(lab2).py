# BFS문제
# 2. M개 선택 가능, 전파에 걸리는 최소 시간
from collections import deque
import itertools
from copy import deepcopy
N, M = map(int, input().split())


def bfs():
    # 전파시간을 저장할 배열
    time = [[0 for _ in range(N)] for _ in range(N)]

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if lab2[x + dx][y + dy] == 0:
                    time[x + dx][y + dy] = time[x][y] + 1  # 시간 체크
                    lab2[x + dx][y + dy] = 2  # 방문처리
                    q.append((x + dx, y + dy))  # 큐에 넣기

    # 시간 카운트
    tof = False  # 0이 있는지 여부
    res = 0
    for i in range(N):
        for j in range(N):
            if lab2[i][j] == 0:
                tof = True
            res = max(time[i][j], res)  # 전파시간 최댓값 갱신

    if tof:  # 0이 있으면 모든 구역에 전파되지 않은 것이므로
        return -1
    else:
        return res



# 바이러스 위치 저장
v = []
q = deque()
# 바이러스 전파에 걸리는 최소 시간
temp = float('inf')

# 연구소 초기 상태 저장
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스의 좌표 저장
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            v.append((i, j))  # 좌표를 저장하고
            lab[i][j] = 0  # 해당 위치는 0으로 바꿈

# 바이러스 위치 중 가능한 M개를 뽑는 조합 - 백트래킹은 시간초과;
for comb in itertools.combinations(range(len(v)), M):
    lab2 = deepcopy(lab)
    for idx in comb:
        x, y = v[idx]
        lab2[x][y] = 2
        q.append(v[idx])
    t = bfs()
    if t != -1:  # 모두 전파가능한 경우만
        temp = min(t, temp) # 기존값과 비교하여 갱신

print(temp if temp != float("inf") else -1)