import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []  # 최소힙을 구현할 우선순위 큐
for _ in range(N):
    q = int(input())
    if q:  # 0이 아니면
        heapq.heappush(pq, q)
    else:  # 0이면
        if pq:
            num = heapq.heappop(pq)
            print(num)
        else:
            print(0)