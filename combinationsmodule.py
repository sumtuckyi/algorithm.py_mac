from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    p = list(map(int, input().split()))
    stations = [i for i in range(N)]
    max_v = 0

    for comb in combinations(stations, 4):
        li = list(comb)
        temp = []

        for sub in combinations(li, 2):
            temp.append(list(sub))

        for i in range(3):  # 3회 반복
            a, b = temp[i]
            x, y = temp[5-i]
            a, b = min(a, b), max(a, b)
            x, y = min(x, y), max(x, y)
            # print(a, b, x, y)
            # 인접 하면 패스

            if (
                    (abs(a - b) == 1 or abs(a - b) == N - 1) or
                    (abs(x - y) == 1 or abs(x - y) == N - 1) or
                    (abs(a - y) == 1 or abs(a - y) == N - 1) or
                    (abs(b - x) == 1 or abs(b - x) == N - 1) or
                    (abs(a - x) == 1 or abs(a - x) == N - 1) or
                    (abs(b - y) == 1 or abs(b - y) == N - 1)
            ): continue
                # 조건을 만족하는 경우에 수행할 작업
            # print(a, b, x, y)
            # 교차 하면 패스
            if (x < a < y <b) or (a < x < b < y):
                continue

            cur_v = (p[a] + p[b])**2 + (p[x] + p[y])**2
            max_v = max(max_v, cur_v)
            # print(a, b, x, y)
        # print(temp)
        # 4개의 역을 그룹으로 나누는 모든 경우의 수 고려하기(3가지)
        # for i in range(1, 4):
        #     a, b = li[0], li[i]
        #     x, y = li[]
        #     a, b = max(a, b), min(a, b)
        #     x, y = max(x, y), min(x, y)
        #     # 인접 하면 패스
        #     if ((abs(a-b) == 1 or N-1) or (abs(x-y) == 1 or N-1) or (abs(a-y) == 1 or N-1) or (abs(b-x) == 1 or N-1) or (abs(a-x) == 1 or N-1) or (abs(b-y) == 1 or N-1)):
        #         continue
        #     # 교차 하면 패스
        #     if (x < a < y <b) or (a < x < b < y):
        #         continue
        #     cur_v = (p[a] + p[b])**2 + (p[x] + p[y])**2
        #     max_v = max(max_v, cur_v)

    print(f'#{tc} {max_v}')
