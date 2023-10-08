import sys
from collections import deque

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())  # 출발점과 도착점
visited = [0 for _ in range(N)]
# distance = abs(a-b) # 점프해야할 거리
num = li[a - 1]  # 출발점의 값
q = deque([(a, 0)])  # 출발점과 누적 점프횟수
visited[a-1] = 1 #시작점 방문
ans = -1
tof = False
# 큐에 삽입한 값을 새로운 기준점으로 계속해서 탐색(양방향)
new_r = 0
new_l = 0
while q:
    now, cnt = q.popleft()
    # print(now, cnt)
    cur = li[now - 1]  # 현위치에 적힌 값
    # print(cur,'의 배수 만큼만 이동한다.')
    n = 0  # 배수 계산을 위해 곱해줄 값
    # 오른쪽으로 이동 가능한 경우를 모두 고려
    while True:
        n += 1  # 다음으로 큰 배수 만큼 이동
        new_r = now + cur * n  # 현위치에서 방문 가능한 돌의 번호
        # print('new_r', new_r)
        if new_r == b: # 목적지에 도착했으면 중단
            ans = cnt + 1
            tof = True
            break
        if new_r <= N:  # 범위 내에 있다면
            if not visited[new_r - 1]:
                q.append((new_r, cnt + 1))
                visited[new_r - 1] = 1
        else: # 범위를 벗어났다면 이동 중단
            # print(q)
            break

    if tof:  # 오른쪽으로 한 번 더 이동하다 b에 도착한 경우이면
        break
    # 왼쪽으로 이동 가능한 경우를 모두 고려
    # print('왼쪽으로 이동')
    m = 0
    while True:
        m += 1
        new_l = now - cur * m
        # print('new_l', new_l)
        if new_l == b:
            ans = cnt + 1
            tof = True
            break
        if new_l >= 1:
            if not visited[new_l - 1]:
                q.append((new_l, cnt + 1))
                visited[new_l] = 1
        else:
            break
    if tof:  # 왼쪽으로 한 번 더 이동하다 b에 도착한 경우이면
        break

print(ans)


