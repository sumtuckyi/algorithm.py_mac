# dfs로 접근 시에 시간초과, 다익스트라로 접근
import heapq

idx = 1

while True:
    N = int(input())

    if N == 0:
        exit()

    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)


    res = [10**10]
    # dis[i][j]는 (0, 0)부터 (i, j)까지의 최소 비용
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]

    def dijkstra(start_x, start_y):
        pq = [(grid[start_x][start_y], start_x, start_y)]
        dist[start_x][start_y] = grid[start_x][start_y]

        while pq:
            cost, cur_x, cur_y = heapq.heappop(pq)

            if dist[cur_x][cur_y] < cost:
                continue

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = cur_x + dx, cur_y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                n_cost = cost + grid[nx][ny]
                if n_cost >= dist[nx][ny]:
                    continue
                dist[nx][ny] = n_cost
                heapq.heappush(pq, (n_cost, nx, ny))


    dijkstra(0, 0)
    print(f'Problem {idx}: {dist[N-1][N-1]}')
    idx += 1

