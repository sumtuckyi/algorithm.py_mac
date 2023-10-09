import sys
from collections import deque


def get_distance(home, li):  # 집의 위치 좌표 리스트와 M개의 치킨집 번호 리스트
    total = 0  # 마을의 치킨 거리의 합
    for now_x, now_y in home:
        min_d = float('inf')
        for num in li:
            a, b = kfc[num] # 치킨집의 좌표
            dist = abs(now_x-a) + abs(now_y-b)
            if min_d > dist:
                min_d = dist
        total += min_d  # 각 집의 치킨 거리를 더해주기
    return total


# M개의 치킨집 선택(bt)
def back_t(level, survived, num):
    global ans
    if level == M:
        ans = min(ans, get_distance(home, survived))
        return

    # 조합 구현
    for i in range(num+1, C):
        if visited[i]: # 이미 선택된 치킨집이면 패스
            continue
        visited[i] = 1
        back_t(level + 1, survived + [i], i)
        visited[i] = 0  # 원상복구


N, M = map(int, sys.stdin.readline().split())
kfc = deque()
home = deque()
ans = float('inf')
for i in range(N):
    row = list(sys.stdin.readline().split()) # 문자열로 저장
    for j in range(N):
        # 치킨집의 좌표 저장
        if row[j] == '2':
            kfc.append((i, j))
        # 집의 좌표 저장
        if row[j] == '1':
            home.append((i, j))

C = len(kfc) # 치킨집의 개수
visited = [0 for _ in range(C)]
back_t(0, [], -1)
print(ans)