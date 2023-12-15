T = int(input())


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x <= N-1 and 0 <= y <= N-1


def is_any_other_core(x, y, d):
    if d == 0:
        for i in range(0, y):
            if processor[x][i] != 0:
                return -1
        for i in range(0, y):
            processor[x][i] = 2
        return y
    elif d == 1:
        for i in range(0, x):
            if processor[i][y] != 0:
                return -1
        for i in range(0, x):
            processor[i][y] = 2
        return x
    elif d == 2:
        for i in range(y+1, N):
            if processor[x][i] != 0:
                return -1
        for i in range(y + 1, N):
            processor[x][i] = 2
        return N-(y+1)
    else:
        for i in range(x+1, N):
            if processor[i][y] != 0:
                return -1
        for i in range(x + 1, N):
            processor[i][y] = 2
        return N-(x+1)


def rollback(x, y, d):
    cx, cy = x + dx[d], y + dy[d]
    while in_range(cx, cy):
        processor[cx][cy] = 0
        cx += dx[d]
        cy += dy[d]


def backtracking(idx, length, cnt):
    # print(f'백트래킹 함수 시작, index={idx}, length={length}, cnt={cnt}', processor)
    global ans, max_cnt

    # 가지치기
    if cnt > max_cnt:
        max_cnt = cnt
        ans = length
        # print('최대코어개수 갱신됨', max_cnt, length, processor)
    elif cnt == max_cnt:
        ans = min(length, ans)
    # 종료 조건
    if idx == len(core_list):
        return

    # 해당 코어를 기준으로 4방향 탐색
    for i in range(4): # i가 4방향을 나타냄
        # print('현재 방향', i)
        # 현재 탐색 중인 코어의 좌표
        cx, cy = core_list[idx][0], core_list[idx][1]
        # 해당 방향으로 연결이 불가능한 경우 -> 다른 방향 탐색
        can_connect = is_any_other_core(cx, cy, i)
        # print('현재 맵', processor)
        if can_connect == -1:
            continue
        # 연결이 가능한 경우 -> 전선의 길이를 계산, 맵에 연결 상태를 표시
        else:
            # print(f'{idx}에서 추가되는 전선의 길이{can_connect}이고 총 코어 개수는 {cnt + 1}')
            # print("length 갱신", length + can_connect)
            backtracking(idx + 1, length + can_connect, cnt + 1)
            rollback(cx, cy, i)
            # print('롤백 이후', processor)
    # 해당 코어를 연결하지 않고 다음 코어를 고려하는 경우
    backtracking(idx + 1, length, cnt)


for tc in range(1, T + 1):
    N = int(input())
    processor = [list(map(int, input().split())) for _ in range(N)]
    core_list = []
    ans = float("inf") # 전선 길이 합의 최솟값
    max_cnt = 0 # 연결된 코어 개수의 최댓값
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N-1 or j == N-1:
                continue
            elif processor[i][j] == 1:
                core_list.append((i, j))
    backtracking(0, 0, 0)
    print(f'#{tc} {ans}')