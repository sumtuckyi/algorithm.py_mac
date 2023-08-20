from collections import deque
def bfs():
    q = deque([(S, 0)])
    visited = set()
    while q:
        cn, cnt = q.popleft()
        if cn == D:  # 큐에서 꺼낸 값이 목표값인 경우
            return cnt
        if cn in visited:
            continue
        else:
            visited.add(cn)
            if cn:
                q.append((cn // 2, cnt + 1))
            if cn <= 1e5//2:
                q.append((cn * 2, cnt + 1))
            if cn < 1e5:
                q.append((cn + 1, cnt + 1))
            if cn >= 1:
                q.append((cn - 1, cnt + 1))


S = int(input())  # 현재 채널
D = int(input())  # 목표 채널

print(bfs())