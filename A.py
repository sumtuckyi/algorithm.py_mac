from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 역의 개수
    p = list(map(int, input().split()))
    stations = [i for i in range(N)]
    temp = set()
    max_v = 0
    comb_generator = list(combinations(stations, 4))

    for comb in comb_generator:  # 4개의 역을 지정
        nodes_generator = list(combinations(comb, 2))  # 4개 중 두 개 뽑기(총 6가지 경우이고 중복을 제하면 3가지임)
        for nodes in nodes_generator:  # 4개를 두 구간으로 나누기(총 6가지)
            a = set(nodes)  # 한 구간
            b = set(comb) - a  # 나머지 구간
            a1, a2 = min(a), max(a)
            b1, b2 = min(b), max(b)
            if a2 - a1 == N-1 or b2 - b1 == N-1:
                continue
            if a2 - a1 == 1 or b2 - b1 == 1:
                continue
            if (a2 > b2 and a1 < b1) or (a2 < b1):  # a구간이 b구간을 포함하는 경우이거나 만나지 않는 경우
                # if a2 - a1 > 1 and b2 - b1 > 1:  # 두 구간 모두 각각 인접한 역을 연결한 것이 아니고
                    # 각 구간이 인접하지 않은 경우라면
                if abs(a2 - b2) > 1 and abs(a2 - b1) > 1 and abs(a1 - b2) > 1 and abs(a1 - b1) > 1:
                    if max_v < (p[a2]+p[a1])**2 + (p[b2]+p[b1])**2:
                        max_v = (p[a2]+p[a1])**2 + (p[b2]+p[b1])**2

    print(f'#{tc} {max_v}')


from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 역의 개수
    p = list(map(int, input().split()))
    stations = [i for i in range(N)]
    max_v = 0
    comb_generator = combinations(stations, 4)

    for comb in comb_generator:  # 4개의 역을 지정
        nodes_generator = list(combinations(comb, 2))[:3]  # 4개 중 두 개 뽑기(총 6가지 경우이고 중복을 제하면 3가지임)
        for nodes in nodes_generator:  # 4개를 두 구간으로 나누기(총 6가지)
            a = set(nodes)  # 한 구간
            b = set(comb) - a  # 나머지 구간
            a1, a2 = min(a), max(a)
            b1, b2 = min(b), max(b)
            if a2 - a1 == N-1 or b2 - b1 == N-1: # 인접한 역을 이은 구간 제외
                continue
            if a2 - a1 == 1 or b2 - b1 == 1: # 인접한 역을 이은 구간 제외2
                continue
            if abs(a2 - b2) == 1 or abs(a2 - b1) == 1 or abs(a1 - b2) == 1 or abs(a1 - b1) == 1:
                continue
            if (a2 > b2 and a1 < b1) or (a2 < b1):  # a구간이 b구간을 포함하는 경우이거나 만나지 않는 경우
                # if a2 - a1 > 1 and b2 - b1 > 1:  # 두 구간 모두 각각 인접한 역을 연결한 것이 아니고
                    # 각 구간이 인접하지 않은 경우라면

                # if abs(a2 - b2) > 1 and abs(a2 - b1) > 1 and abs(a1 - b2) > 1 and abs(a1 - b1) > 1:
                if max_v < (p[a2]+p[a1])**2 + (p[b2]+p[b1])**2:
                    max_v = (p[a2]+p[a1])**2 + (p[b2]+p[b1])**2

    print(f'#{tc} {max_v}')

