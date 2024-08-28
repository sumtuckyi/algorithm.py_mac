# bfs로 섬 식별, 다른 방법 없을까 - 1905
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m, n = len(grid1), len(grid1[0])
        visited = [[False] * n for _ in range(m)]
        delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islands = []

        def find_island(x, y):
            q = deque()
            q.append([x, y])
            island = [[x, y]]
            visited[x][y] = True

            while q:
                cur_x, cur_y = q.popleft()
                for dx, dy in delta:
                    nxt_x, nxt_y = cur_x + dx, cur_y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n:
                        continue
                    if visited[nxt_x][nxt_y]:
                        continue
                    if grid2[nxt_x][nxt_y] == 0:
                        continue

                    q.append([nxt_x, nxt_y])
                    island.append([nxt_x, nxt_y])
                    visited[nxt_x][nxt_y] = True

            return island

        # grid2를 탐색
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if grid2[i][j] == 0:
                    continue
                island = find_island(i, j)
                islands.append(island)

        res = 0
        for island in islands:
            cnt = 0
            for cell in island:
                x, y = cell[0], cell[1]
                if grid1[x][y] == 0:
                    continue
                cnt += 1
            if cnt == len(island):
                res += 1

        # print(islands)
        return res