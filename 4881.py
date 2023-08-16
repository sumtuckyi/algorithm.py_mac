# 백트래킹 문제


def back_tracking(level, total, x):
    global min_v
    if level == N and x == N:
        if min_v > total:
            min_v = total
        return
    # total += arr[level][]
            # if visited_y[j] == 1:
            #     continue
            # visited_y[j] = 1
            # total += arr[i][j]
            # print(total)
            # back_tracking(level+1, total, x+1)
            # visited_y[j] = 0
            # total -= arr[i][j]
            # back_tracking(level, total, x)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_set = [i for i in range(0, N)]
    min_v = 99
    arr = [list(map(int, input().split()))for _ in range(N)]
    back_tracking(0, 0, 0)
    print(f'#{tc} {min_v}')