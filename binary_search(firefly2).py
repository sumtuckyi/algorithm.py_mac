# 이진 탐색으로 풀기
import sys


def bi_search(arr, target): # target보다 크거나 같은 값 중 최소 인덱스를 반환-> 크거나 같은 값이 없다면 마지막 인덱스를 반환
    s, e = 0, max_ob - 1  # 탐색의 시작점과 종료점
    result = max_ob
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] >= target:
            result = mid
            # 더 앞쪽에 중복값이 있을 수 있으니 왼쪽을 범위로 재탐색
            e = mid - 1
        else:  # 목표값보다 더 작다면
            s = mid + 1
    return result


N, H = map(int, sys.stdin.readline().split())
top = [0 for _ in range(N//2)]
bottom = [0 for _ in range(N//2)]
max_ob = N//2
ans = float('inf')  # 장애물의 최솟값
cnt = 0
for i in range(N):
    height = int(sys.stdin.readline())
    if i % 2 == 0:  # 짝수 번째 장애물
        bottom[i//2] = height
    else:
        top[i//2] = height
# 이진탐색을 위한 데이터 정렬
bottom.sort()
top.sort()

# 모든 구간 탐색
for j in range(1, H + 1):
    top_ob = max_ob - bi_search(top, H+1-j)  # 종유석
    bottom_ob = max_ob - bi_search(bottom, j)  # 석순
    total = top_ob + bottom_ob
    if ans > total:
        ans = total
        cnt = 1
    elif ans == total:
        cnt += 1

print(ans, cnt)