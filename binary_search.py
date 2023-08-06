# 재귀함수를 이용하여 이진탐색 구현하기
def binary_search(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binary_search(a, low, middle - 1, key)
        elif a[middle] < key:
            return binary_search(a, middle + 1, high, key)

a = binary_search([1, 2, 3, 4, 5, 6, 7], 0, 6, 9)
print(a)

# 이진 탐색 문제
