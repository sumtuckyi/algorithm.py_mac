#소프티어 - 나무섭지

import sys
from collections import deque

n, m = map(int, input().split())
grid = []
ghosts = deque()
goal = []
human = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
visited_g = [[0 for _ in range(m)] for _ in range(n)]
delta = [[0, -1], [-1, 0], [0, 1], [1, 0]]

for i in range(n):
    row = list(input())
    grid.append(row)
    for j in range(m):
        if row[j] == 'G':
            ghosts.append([i, j])
            visited_g[i][j] = 1
        elif row[j] == 'D':
            goal.append([i, j])
        elif row[j] == 'N':
            human.append([i, j])
            visited[i][j] = 1


def bfs_for_ghost():
    q = ghosts
    while q:
        coords = q.popleft()
        x, y = coords[0], coords[1]
        for dx, dy in delta:
            cur_x, cur_y = x + dx, y + dy
            if 0 <= cur_x <= n - 1 and 0 <= cur_y <= m - 1:
                if visited_g[cur_x][cur_y] == 0:
                    visited_g[cur_x][cur_y] = visited_g[x][y] + 1
                    ghosts.append([cur_x, cur_y])


def bfs_for_human():
    q = human
    while q:
        coords = q.popleft()  # 전단의 요소부터 꺼내기
        x, y = coords[0], coords[1]
        for dx, dy in delta:
            cur_x, cur_y = x + dx, y + dy
            if 0 <= cur_x <= n - 1 and 0 <= cur_y <= m - 1:
                if grid[cur_x][cur_y] == 'G' or grid[cur_x][cur_y] == '#':
                    continue
                if visited_g[cur_x][cur_y] <= visited[x][y] + 1:
                    continue
                if visited[cur_x][cur_y]:
                    continue
                visited[cur_x][cur_y] = visited[x][y] + 1
                human.append([cur_x, cur_y])


bfs_for_ghost()
bfs_for_human()
# print(visited)
if visited[goal[0][0]][goal[0][1]]:
    print("Yes")
else:
    print("No")
# print(visited_g)


