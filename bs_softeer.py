import sys

n, q = map(int, input().split())
cars = list(map(int, input().split()))

# 중앙값이 m이기 위해서는 m보다 큰 수와 작은 수가 각각 1개 이상 존재해야하며, 그 경우의 수는 b(큰)*s(작은)
# 자동차의 수는 최대 5만 대
# 연비의 범위가 최대 천 만인 걸로 봐서 이진탐색으로 연비의 대소를 비교해야함..동일한 연비는 주어지지 않는다고 가정

cars.sort() # 오름차순으로 정렬
# print(cars)

def cal_ans(q): # q의 인덱스 찾기 -> 그보다 작은 값의 수와 큰 값의 수를 구할 수 있음
    s, e = 0, len(cars)-1
    while s <= e:
        mid = (s + e) // 2 # 루프돌 때마다 mid 갱신해줘야지!!
        if cars[mid] == q:
            print("found it", mid)
            return mid
        elif cars[mid] > q:
            e = mid - 1
        else:
            s = mid + 1
    return None

print(cal_ans(2))
# for _ in range(q):
#     target = int(input())
#     idx = 0
#     # idx = cal_ans(target)
#     if idx is None:
#         print(0)
#     else:
#         lower = idx
#         upper = len(cars) - 1 - idx
#         print(lower*upper)