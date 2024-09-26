from collections import deque


N = int(input())
q = deque((range(1, N + 1)))

while len(q) > 1:
    q.popleft()  # 카드를 버린다.
    if q:
        nxt = q.popleft()
        q.append(nxt)

print(*q)