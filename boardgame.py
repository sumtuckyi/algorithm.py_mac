T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = "NO"

    def check_direction(y, x, dy, dx):
        cnt = 0
        while 0 <= y < N and 0 <= x < N:
            if board[y][x] == 'o':
                cnt += 1
                if cnt == 5:
                    return True
            else:
                cnt = 0
            y += dy
            x += dx
        return False
    # 행 탐색
    for i in range(N):
        if check_direction(i, 0, 0, 1):
            result = "YES"
            break

    # 열 탐색
    for i in range(N):
        if check_direction(0, i, 1, 0):
            result = "YES"
            break

    # 대각선 탐색(우하향)
    for i in range(N):
        if check_direction(i, 0, 1, 1):
            result = "YES"
            break
    for i in range(1, N):
        if check_direction(0, i, 1, 1):
            result = "YES"
            break

    # 대각선 탐색(우상향)
    for i in range(N):
        if check_direction(i, 0, -1, 1):
            result = "YES"
            break
    for i in range(1, N - 1):
        if check_direction(N - 1, i, -1, 1):
            result = "YES"
            break

    print(f'#{tc} {result}')