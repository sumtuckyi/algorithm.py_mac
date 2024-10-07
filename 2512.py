N = int(input())  # 지방의 수

regions = list(map(int, input().split()))
M = int(input())  # 총 예산
answer = 0
# 요청액의 합이 총예산보다 크지 않다면
if sum(regions) <= M:
    answer = max(regions)
else: # 총예산보다 크다면
    pass