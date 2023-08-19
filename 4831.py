T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    bus_stops = [0] * (N + 1)
    cnt = 0
    zeros = 1
    total = 0
    is_possible = True
    for i in stations:
        bus_stops[i] = 1

    # 종점에 도착할 수 없는 경우
    for i in range(0, N):
        if bus_stops[i] == bus_stops[i + 1] == 0:
            zeros += 1
            if zeros == K:
                is_possible = False
        else:
            zeros = 1

    # 종점에 도착할 수 있는 경우
    if is_possible:
        current = 0
        while current < N:
            if current + K >= N:
                break
            elif bus_stops[current + K] == 1:
                current += K
                cnt += 1
            else:
                for i in range(K - 1, 0, -1):
                    if bus_stops[current + i] == 1:
                        current += i
                        cnt += 1
                        continue
    if is_possible:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc}', 0)


