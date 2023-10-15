# hide_n_seek4
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
# 시작부터 둘의 위치가 같은 경우
if N == K:
    print(0)
    print(N)
    exit()
elif N > K:
    li = [i for i in range(N, K-1, -1)]
    print(N-K)
    print(*li)
    exit()
else:
    q = deque()  # 수빈이의 가능한 위치
    q.append(N)
    visited = [-1 for _ in range(100_001)]  # 해당 지점까지 도착하기까지의 최소 시간
    tracked = [-1 for _ in range(100_001)]  # tracked[i] = i에 도착하기 바로전 위치
    visited[N] = 0  # 수빈이의 초기 위치 방문 처리 - 출발점이므로 0초 소요
    while q:
        cur = q.popleft()  # 출발점, 해당 출발점까지의 소요시간
        if cur == K:
            break
        for nest in [cur * 2, cur + 1, cur - 1]:
            if 0 <= nest <= 100_000:
                if visited[nest] == -1:  # 도착점을 아직 방문한 적이 없다면
                    visited[nest] = visited[cur] + 1
                    tracked[nest] = cur
                    q.append(nest)
    # recursionError 발생함
    # def find(n):
    #     if tracked[n] == N:
    #         path.append(N)
    #         return
    #     else:
    #         path.append(tracked[n])
    #         find(tracked[n])

    path = []
    p = K
    while p != N:
        path.append(p)
        p = tracked[p]
    path.append(N)
    # find(K)
    print(visited[K])
    print(*path[::-1])
