N = int(input())  # 지방의 수

regions = list(map(int, input().split()))
M = int(input())  # 총 예산
MAX = 0
# 요청액의 합이 총예산보다 크지 않다면
if sum(regions) <= M:
    print(max(regions))
else:  # 총예산보다 크다면
    # 정수 상한액을 정하고, 이를 넘는 지방에는 상한액 만큼만 지급한다.
    l, r = M // N,  max(regions)

    while l <= r:
        mid = (l + r) // 2  # 정수 상한액
        total = 0
        for region in regions:
            if region <= mid: # 상한액 이하이면 원래 예산을 지급
                total += region
            else:  # 상한액 초과이면 상한액만 받을 수 있음
                total += mid

        if total > M: # 정수 상한액이 mid일 때, 총 지급액이 예산을 넘어가면
            r = mid - 1
        else: # 총 지급액이 예산과 같거나 더 적으면
            MAX = max(MAX, mid)  # 현재까지의 최대 상한액을 기록
            l = mid + 1


    print(MAX)

