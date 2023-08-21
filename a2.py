from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    p = list(map(int, input().split()))
    stations = [i for i in range(N)]
    max_v = 0

    for comb in combinations(stations, 4):
        a2, a1 = max(comb), min(comb)
        b2, b1 = N-1 - a2, N-1 - a1
        if a2 - a1 == 1 or b2 - b1 == 1:
            continue
        if (a2 > b2 and a1 < b1) or (a2 < b1):
            if abs(a2 - b2) > 1 and abs(a2 - b1) > 1 and abs(a1 - b2) > 1 and abs(a1 - b1) > 1:
                cur_v = (p[a2] + p[a1])**2 + (p[b2] + p[b1])**2
                max_v = max(max_v, cur_v)

    print(f'#{tc} {max_v}')
