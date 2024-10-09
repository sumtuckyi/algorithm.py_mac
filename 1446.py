# 다익스트라
# 0지점에서 1씩 이동하다가 지름길의 시작점을 만나면 목적지까지의 최단 거리 갱신
import heapq


def optimize_path(N, D, shortcut):
    shortcut.sort()

    # 거리 배열 초기화
    distance = [i for i in range(D + 1)]

    # 우선순위 큐 초기화
    pq = [(0, 0)]  # (현재까지의 거리, 현재 위치)

    while pq:
        dist, curr = heapq.heappop(pq)

        # 목적지에 도달했다면 종료
        if curr == D:
            return dist

        # 현재 위치에서 다음 위치로 이동
        if curr + 1 <= D and dist + 1 <= distance[curr + 1]:
            distance[curr + 1] = dist + 1
            heapq.heappush(pq, (dist + 1, curr + 1))

        # 지름길 확인
        for start, end, length in shortcut:
            if start == curr and end <= D and dist + length < distance[end]:
                distance[end] = dist + length
                heapq.heappush(pq, (dist + length, end))

    return distance[D]


N, D = map(int, input().split())

shortcut= [] # 겹치지 않는 지름길만 남기기
for _ in range(N):
    s, e, dist = map(int, input().split())
    if e > D: # 지름길 도착점이 고속도로를 넘어가면 패스
        continue
    if (e - s) <= dist:  # 지름길이 더 짧지 않으면 패스
        continue
    shortcut.append((s, e, dist))  # 단축거리, 시작, 끝 저장



res = optimize_path(N, D, shortcut)
print(res)
