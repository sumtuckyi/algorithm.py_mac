numbers = [17, 3, 7, 1, 11, 30, 21, 0]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):  # len(arr) - 1 번의 패스
        for j in range(0, i):  # 각 패스 마다 비교를 반복
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(numbers)
print(numbers)