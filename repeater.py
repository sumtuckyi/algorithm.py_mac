import math
T = int(input())


def distance(y, x, hy, hx):
    D = (abs(y-hy))**2 + (abs(x-hx))**2  # 중계기와 집 사이 거리의 제곱
    return math.sqrt(D)


for tc in range(1, T + 1):
    N = int(input())  # 지도의 크기
    map_data = [list(map(int, input().split())) for _ in range(N+1)]  # 마을 지도
    d_set = set()
    for i in range(N+1):
        for j in range(N+1):
            if map_data[i][j] == 2:
                y, x = i, j

    for i in range(N+1):
        for j in range(N+1):
            if map_data[i][j] == 1:
                d_set.add(distance(y, x, i, j))

    print(f'#{tc} {math.ceil(max(d_set))}')