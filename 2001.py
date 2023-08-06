T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    def catch_fly(y, x):
        total = 0
        for i in range(M):
            for j in range(M):
                if 0 <= y + i < N and 0 <= x + j < N:
                    total += board[y + i][x + j]
        return total

    for i in range(N):
        for j in range(N):
            if max_v < catch_fly(i, j):
                max_v = catch_fly(i, j)

    print(f'#{tc} {max_v}')