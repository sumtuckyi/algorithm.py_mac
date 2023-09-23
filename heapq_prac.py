# 최소힙에 리스트를 추가하면 0번째 인덱스를 기준으로 정렬하되, 그 값이 동일한 경우 그 다음 인덱스의 값을 기준으로 정렬
import heapq

n = int(input())
bars = list(map(int, input().split()))
min_heap = []
for i in range(len(bars)):
    heapq.heappush(min_heap, [bars[i], -1])
cnt = 0

while min_heap:
    # 첫 번째로 가벼운 물건 꺼내기
    first, gos = heapq.heappop(min_heap)
    if gos == -1:  # 꺼낸 물건이 황금이면
        cnt += 1
    else:  # 짱돌이면
        break
    # 두 번째로 가벼운 물건 꺼내기
    fake, gos = heapq.heappop(min_heap)
    if gos == -1:
        cnt += 1
    else:
        break
    # 짱돌 넣기
    heapq.heappush(min_heap, [fake*2, 0])

print(cnt)

