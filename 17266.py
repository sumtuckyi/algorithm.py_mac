# 이진탐색 기초
N = int(input())
M = int(input())
pos = list(map(int, input().split()))
ans = float('inf')
l, r = 1, N

# 거리를 미리 계산
dist = []
for i in range(1, M):  #(M-1)개 구간
    d = pos[i] - pos[i - 1]
    dist.append(d)
# dist = dist + [N - pos[-1]]

while l <= r:
    mid = (l + r) // 2
    is_possible = True
    # 모든 길을 비출 수 있는지 확인
    while True:
        if pos[0] > mid or (N - pos[-1]) > mid:
            is_possible = False
            break
        for d in dist:
            if d > mid * 2:
                is_possible = False
                break
        break

    if not is_possible:  # mid를 높인다.
        l = mid + 1
    else:  # mid를 낮춘다.
        ans = min(ans, mid)
        r = mid - 1

print(ans)