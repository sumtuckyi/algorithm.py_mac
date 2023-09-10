def bfs(x, y):  # 탐색 시작점을 인자로 받음
    global cnt, last
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + i < N and 0 <= y + j < N:
            if b[x][y] + 1 == b[x+i][y+j]:
                cnt += 1
                bfs(x+i, y+j)

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    b = [list(map(int, input().split())) for _ in range(N)]
    max_v, temp, max_n = -1, 0, 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            result = bfs(i, j)  # 해당점을 시작으로 연결된 방의 수
            if result > max_v:
                max_v = result
                max_n = b[i][j]  # 시작 방 번호
                temp = max_n + result  # 연결된 방 중 가장 큰 번호
            elif result == max_v:
                max_n = min(b[i][j], max_n)
    print(f'#{tc} {max_n} {max_v+1}')



