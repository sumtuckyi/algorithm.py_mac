from collections import deque

N = int(input())
M = int(input())

adj_mat = []
for _ in range(N):
    row = list(map(int, input().split()))
    adj_mat.append(row)

path = list(map(int, input().split())) # 여행경로

def is_connected(a, b): # a와 b가 연결되어 있는지 판단
    q = deque()
    q.append(a - 1)
    vis = [False]*(N + 1)
    while q:
        n = q.popleft()
        if n == b - 1:
            return True
        vis[n] = True
        for i in range(N):
            if adj_mat[n][i] == 0 or vis[i]:
                continue
            q.append(i)
    return False

dup_check = set()
# 여행 경로의 모든 구간을 확인
for i in range(len(path) - 1):
    v = (path[i], path[i+1])
    v = tuple(sorted(v))
    if v in dup_check:
        continue
    if is_connected(v[0], v[1]):
        dup_check.add(v)
    else:
        print('NO')
        exit()

print('YES')