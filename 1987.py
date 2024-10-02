# 이미 지나온 알파벳과 동일한 칸은 지나갈 수 없다.
# 시작점을 포함하여 말이 지날 수 있는 최대 칸의 수를 출력하라

# 방문체크 필요, 이동 가능 여부 판별 시에 set이용 -> 비트마스킹을 사용하여 방문한 알파벳을 추적, 각 비트는 하나의 알파벳
# dfs 사용 - 재귀 or 스택
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(input())
vis = [[False for _ in range(C)] for _ in range(R)]
MAX = [0]

def dfs(p, q, moves):
    cur_x , cur_y = p, q

    if len(moves) > MAX[0]:
        MAX[0] = len(moves)
    if MAX[0] == 26:
        return
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = cur_x + dx , cur_y + dy
        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            continue
        if vis[nx][ny]:
            continue
        if grid[nx][ny] in moves:
            continue
        vis[nx][ny] = True
        dfs(nx, ny, moves + grid[nx][ny])
        vis[nx][ny] = False


s = grid[0][0]
dfs(0, 0, s)

print(MAX[0])
