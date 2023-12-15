# 산악구조로봇
import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start[0]][start[1]] = 0

    while pq:
        fuel, now = heapq.heappop(pq)
        x, y = now[0], now[1]

        if distance[x][y] < fuel:
           continue

        # 터널이 있는 좌표라면 따로 처리
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + i < N and 0 <= y + j < N:
                next = (x + i, y + j)
                if arr[x][y] < arr[x + i][y + j]:
                    cost = (arr[x + i][y + j] - arr[x][y])*2
                elif arr[x][y] > arr[x + i][y + j]:
                    cost = 0
                else:
                    cost = 1

                new_cost = fuel + cost
                if new_cost >= distance[next[0]][next[1]]:
                    continue
                distance[next[0]][next[1]] = new_cost
                heapq.heappush(pq, (new_cost, next))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    dijkstra((0, 0))
    print(f'#{tc} {distance[N-1][N-1]}')
