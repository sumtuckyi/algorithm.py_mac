# BFS문제
# 2. M개 선택 가능, 전파에 걸리는 최소 시간
# 3.비활성 바이러스일지라도 활성 바이러스와 만나면 활성화 됨
from collections import deque
N, M = map(int, input().split()) # 연구소의 크기, 놓을 수 있는 바이러스의 개수
from copy import deepcopy

# 바이러스의 위치 저장
# 바이러스는 최소 M개에서 최대 10개
v = []
q = deque()


# 연구소의 상태
lab = [list(map(int, input().split())) for _ in range(N)]



for i in range(N):
    for j in range(N):
        if lab[i][j] == 2: # 바이러스를 놓을 수 있는 좌표 저장
            v.append((i, j))

# 바이러스 방문체크 배열(3개 뽑기)
visited = [0 for _ in range(len(v))]
# 정답
ans = 0
temp = float('inf')

# M개의 바이러스가 선택되면 시뮬레이션 돌려서 얼마나 걸리는지 체크하기
def bfs(res):
    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    visited3 = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] != 2:  # 0과 1만 저장
                visited2[i][j] = lab[i][j]

    for i in range(len(v)):
        if visited[i]:
            q.append((v[i][0], v[i][1])) # 바이러스의 위치 M개 저장
            visited3[v[i][0]][v[i][1]] = 1 # 활성바이러스는 방문처리
            visited2[v[i][0]][v[i][1]] = 0 # 연구실 복사본, 값을 0으로 - 시간계산을 위함

    while q:  # 탐색시작
        cur_x, cur_y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= cur_x + dx < N and 0 <= cur_y + dy < N:
                if visited3[cur_x + dx][cur_y + dy]:  # 이미 방문한 경우
                    continue
                if visited2[cur_x + dx][cur_y + dy] == 1:  # 벽인 경우
                    visited2[cur_x + dx][cur_y + dy] = '-'
                    visited3[cur_x + dx][cur_y + dy] = 1 # 방문처리
                    continue
                # 아직 방문하지 않은 0인 경우
                visited3[cur_x + dx][cur_y + dy] = 1  # 방문처리
                q.append((cur_x + dx, cur_y + dy))
                visited2[cur_x + dx][cur_y + dy] = visited2[cur_x][cur_y] + 1

    tof = False
    # 바이러스 전파 여부 확인
    for i in range(N):
        for j in range(N):
            if visited2[i][j] != '-': # 벽이 아닌 경우만 카운트
                # res = max(res, visited2[i][j])
                # 가지치기
                if visited2[i][j] >= temp:
                    tof = not tof
                    break
                if visited2[i][j] == 0: # 바이러스가 퍼지지 않은 칸 + 근원지
                    cnt += 1
        if tof:
            return temp
    if cnt == M:
        return res
    else:
        return -1


# len(v)개의 바이러스 중 M개를 고르는 경우별로 걸리는 시간 카운트
def dfs(depth):
    global temp
    if depth == M:
        t = bfs(float('-inf'))
        if t != -1:
            temp = min(t, temp)
        return

    for i in range(len(v)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0

dfs(0)
print(temp if temp != float("inf") else -1)
