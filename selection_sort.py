# selection-sort
def selection_sort(a, N):
    for i in range(N - 1):  # swap이 총 N - 1회 발생
        min_idx = i  # 최솟값과 swap될 데이터의 인덱스, swap이 한 번 발생하고 나면 다음 패스에서는 정렬된 데이터의 다음 인덱스부터 반복 시작
        for j in range(i + 1, N):  # 기준이 되는 인덱스의 다음인덱스부터 리스트의 끝까지 비교
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


numbers = [64, 25, 11, 10, 22]
selection_sort(numbers, 5)
print(numbers)

# k번째로 작은 원소를 찾는 알고리즘
