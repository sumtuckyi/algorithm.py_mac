from bisect import bisect, bisect_left
from collections import deque, defaultdict

# 기본 이진탐색 함수
def bi_search(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid

        return None

# 원소의 위치만 찾을 거라면 라이브러리 사용
arr = [i for i in range(1, 11)]
print(bisect_left(arr, 2))