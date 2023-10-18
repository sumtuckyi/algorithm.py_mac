# hide_n_seek5
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
if N == K:
    print(0)
    exit()

# 동생의 위치 배열 채우기
sis = [K] + [-1 for _ in range(1000)]
for i in range(1, 1000+1):
    if sis[i-1] + i <= 500_000:
        sis[i] = sis[i-1] + i
    else: # 동생의 위치가 범위를 넘어서면 배열 채우기 중단
        break

q = deque()
q.append((N, 0))
ans = 0
found = False
while q:
    cur, time = q.popleft() # 5, 0
    for nest in [cur * 2, cur + 1, cur - 1]: # 10, 6, 4
        if 0 <= nest <= 500_000:
            if sis[time + 1] != -1:  # 다음 시간에 동생이 범위 내에 있다면
                if sis[time + 1] == nest:  # 동생과 만난 경우 sis[1] = 18
                    ans = time + 1
                    found = True
                    break
                else: # 동생과 만나지 못한 경우
                    q.append((nest, time + 1)) # (10, 1), (6, 1), (4, 1)
            else: # 다음 시간에 절대 동생을 만나지 못하는 경우
                break
    if found:
        break

if not ans:
    print(-1)
    exit()

print(ans)
print(sis[-1])