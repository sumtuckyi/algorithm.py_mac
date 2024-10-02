N = int(input())

grid = [list(input()) for _ in range(N)]
directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 왼오하상

def is_heart(i, j):
    for dx, dy in directions:
        nx = i + dx
        ny = j + dy
        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
            if grid[nx][ny] != '*':
                return False
        else: # 범위 벗어남
            return False
    return True


def helper_func(x, y, dir):
    dx, dy = directions[dir][0], directions[dir][1]
    cnt = 0 # 시작점 포함 안함
    nx = x + dx
    ny = y + dy
    while 0 <= nx < N and 0 <= ny < N: # 방문할 칸이 범위 안에 있는 한 반복
        if grid[nx][ny] == '*': # 신체부위라면
            cnt += 1
            nx += dx
            ny += dy
        else:
            break
    return cnt


heart = []
# 심장 찾기
for i in range(N):
    for j in range(N):
        if is_heart(i, j):
            heart = [i + 1, j + 1] # 1-base
            break
    if heart:
        break

upper = [] # 왼팔, 오른팔, 허리, 머리
# 길이 측정
for i in range(4):
    upper.append(helper_func(heart[0] - 1, heart[1] - 1, i)) # 0-base로 보정

legs = [0, 0]
# 다리 길이 측정 - 허리 위치 기준
legs[0] = helper_func(heart[0] - 1 + upper[2] + 1, heart[1] - 2,2)
legs[1] = helper_func(heart[0] - 1 + upper[2] + 1, heart[1],2)
print(' '.join(map(str, heart)))
print(upper[0], upper[1], upper[2], legs[0] + 1, legs[1] + 1)

