from collections import deque
N, M = map(int, input().split()) # 연구소의 크기, 세로*가로
from copy import deepcopy
q = deque()
res = float('-inf')

#연구소 상태 받기 - 이걸로 그대로 시뮬레이션 돌릴 것임
lab = [list(map(int, input().split())) for _ in range(N)]
# 벽의 위치 3곳 저장
visited = [[0 for _ in range(M)] for _ in range(N)]
#바이러스 좌표 저장하기


def bfs():
    global res
    visited2 = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 원본배열을 변경하지 않도록 함
            visited2[i][j] = lab[i][j]
            if lab[i][j] == 2:
                q.append((i, j))
    cnt = 0

    while q:
        x, y = q.popleft()
        visited2[x][y] = 1
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                #이미 방문했거나 벽, 바이러스, 새로 세워진 벽이면 패스
                if visited2[x + dx][y + dy] != 0:
                    continue
                # 아직 방문한 적 없는 0인 경우만
                visited2[x + dx][y + dy] = 1
                q.append((x + dx, y + dy))

    # lab2의 0의 개수 카운트
    for i in range(N):
        for j in range(M):
            if visited2[i][j] == 0:
                cnt += 1
    res = max(res, cnt)

def backtracking(depth):
    if depth == 3:
        bfs()
        return

# 0이고 아직 선택되지 않았으면 벽 세우기
    for i in range(N):
        for j in range(M):
            # 빈 곳이 아니거나 이미 뽑은 자리면 패스
            if lab[i][j] != 0 or visited[i][j] == 1:
                continue
            # 그렇지 않다면 방문처리
            visited[i][j] = 1
            lab[i][j] = 1
            backtracking(depth + 1)
            visited[i][j] = 0
            lab[i][j] = 0

backtracking(0)
print(res)
