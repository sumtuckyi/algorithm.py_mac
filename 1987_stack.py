# 스택활용한 dfs 구현 + set 자료구조 사용으로 효율 개선

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(input())


def dfs():
    stack = {(0, 0, grid[0][0])}
    max_moves = 1

    while stack:
        x, y, visited = stack.pop()
        max_moves = max(max_moves, len(visited))

        # 가지치기
        if max_moves == 26:
            return 26

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if grid[nx][ny] in visited:# 새로운 칸의 알파벳
                    continue
                stack.add((nx, ny, visited + grid[nx][ny]))

    return max_moves

print(dfs())