from collections import deque


N, L, R = map(int, input().split())

grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

def bfs(x, y, idx):  # idx는 연합 번호
    q = deque()
    q.append((x, y))
    union[x][y] = idx
    countries = [(x, y)]
    total = grid[x][y]
    count = 1 # 이번 연합에 속한 국가 수

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cur_x + dx, cur_y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if union[nx][ny]:
                continue
            diff = abs(grid[cur_x][cur_y] - grid[nx][ny])
            if diff < L or diff > R:
                continue
            # 여기서 연합 정보 기록, 인구 수 계산, 인구 재분배까지 수행
            union[nx][ny] = idx  # 연합 정보 기록
            q.append((nx, ny))
            countries.append((nx, ny))
            total += grid[nx][ny]
            count += 1

    new_pop = total // count
    for i, j in countries:
        grid[i][j] = new_pop

    return count > 1  # 연합이 생성되었는지 여부를 반환

day = 0
while True:  # 시뮬레이션 시작
    # 1)연합 관계 생성하기
    union = [[0 for _ in range(N)] for _ in range(N)]
    idx = 1
    is_union_formed = False  # 시뮬레이션 중단 여부 판단 플래그

    for i in range(N):
        for j in range(N):
            if union[i][j] == 0:
                if bfs(i, j, idx):
                    is_union_formed = True
                idx += 1

    if not is_union_formed:
        break

    day += 1
    # 연합별 인구 계산
    # pop = [[0, 0] for _ in range(N**2 + 1)]
    # for i in range(N):
    #     for j in range(N):
    #         g = union[i][j]
    #         pop[g][0] += grid[i][j]
    #         pop[g][1] += 1 # 연합에 속한 국가의 수
    # # 인구 이동이 불가능한 상태인지 확인
    # if idx == N**2 + 1:  # 국가의 수만큼 연합이 생성된 경우
    #     break  # 시뮬레이션 종료

    # 인구 수 재조정
    # for i in range(N):
    #     for j in range(N):
    #         g = union[i][j]
    #         grid[i][j] = pop[g][0] // pop[g][1]


print(day)