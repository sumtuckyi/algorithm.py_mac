# 사각지대를 최대한 줄여라..!
import copy


# 1부터 5까지가 cctv
# 1번: 4방향, 2번: 2방향, 3번: 4방향, 4번: 2방향, 5번: 1방향
# cctv는 최대 8개 -> 4^8
def check_area(x, y, dir, vis):  # 탐색 시작 위치(카메라 유형도 알 수 있음), 방향, 방문배열
    cur_x, cur_y = x, y
    c = grid[x][y]  # 카메라 종류
    for dx, dy in d[c - 1][dir]:  # 카메라 방향에 따라 탐색 시작
        nx, ny = cur_x + dx, cur_y + dy
        # 같은 방향으로 나아간다. 벽을 만나거나, 경계를 넘어서면 멈춘다.
        while 0 <= nx < N and 0 <= ny < M:
            if vis[nx][ny] == 6:  # 벽을 만나면 멈춘다.
                break
            if vis[nx][ny] == 0:  # 0이거나 이미 방문한 곳인 경우에만 '#'으로 바꿔준다.
                vis[nx][ny] = '#'  # 방문처리
            nx += dx
            ny += dy

    return vis


def dfs(depth, vis):
    global MAX_CNT
    if depth == C:  # 마지막 cctv이면
        cnt = 0
        for i in range(N):
            for j in range(M):
                if vis[i][j] == 0:
                    cnt += 1
        # 사각지대의 수 갱신
        MAX_CNT = min(MAX_CNT, cnt)
        return

    for i in range(dir_table[cam[depth][0]]):  # cctv유형 별 방향의 가지수 동적 지정
        # print(f'{i}방향')
        new_vis = check_area(cam[depth][1], cam[depth][2], i, copy.deepcopy(vis))
        # print('감시 후 배열', new_vis)
        dfs(depth + 1, new_vis)


N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

dir_table = {
    1: 4,
    2: 2,
    3: 4,
    4: 4,
    5: 1
}

d = [
    [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
    [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, -1), (1, 0)]],
    [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
]

cam = []  # cctv 유형과 위치 정보 저장
cnt = 0  # 0이 아닌 공간의 수
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0 and grid[i][j] != 6:
            cam.append((grid[i][j], i, j))
        if grid[i][j] != 0:
            cnt += 1
vis = copy.deepcopy(grid)
C = len(cam)
MAX_CNT = N*M - cnt  # 초기 0의 개수
# print(cam)
if C:
    dfs(0, vis)

print(MAX_CNT)