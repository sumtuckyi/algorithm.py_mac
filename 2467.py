# 전체 용액의 수는 최대 10만 개
# 투 포인터 접근으로 O(N)으로 해결 가능
# 두 수를 합해서 0에 최대한 가까운 값을 만들려고 한다.
# 오름차순으로 정렬된 순서로 주어진다.

N = int(input())
arr = list(map(int, input().split()))

s, e = 0, len(arr) - 1
liq1, liq2 = s, e
ans = 1e12

while s < e:
    val = arr[s] + arr[e]
    if abs(val) < ans:
        ans = abs(val)
        liq1, liq2 = s, e

    if val < 0:  # 합이 음수인 경우, 0에 가까워지기 위해서는 더 큰 값을 더해야 하므로 s를 오른쪽으로 이동
        s += 1
    elif val > 0: # 합이 양수인 경우, 0에 가까워지기 위해서는 더 작은 값을 더해야 하므로 e를 왼쪽으로 이동
        e -= 1
    else: # 0이면 바로 탐색 종료
        print(arr[s], arr[e])
        exit()

print(arr[liq1], arr[liq2])
