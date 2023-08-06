# bit = [0, 0, 0, 0] # 2 ^ 4 = 16개의 부분집합
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# 부분집합 생성하기 2 + 부분집합 중 주어진 조건을 만족하는 경우를 찾아내기
arr = [-3, 6, 2, 1, -5, 4]
n = len(arr)

cnt = 0
for i in range(1<<n):  # 원소의 개수가 n개일 때 부분집합의 총 개수만큼 반복 작업 수행 (0 ~ 2^n - 1)
    subset = []
    for j in range(n):  # 원소의 개수가 n개일 때 부분집합의 수는 2^n개이므로 최대 n-1자리의 이진수인 i에 대해 각 자리의 비트가 1인지 확인
        if i & (1 << j):  # i의 j번째 비트가 1이 아닌 경우에만 False
            subset.append(arr[j])
    if sum(subset) == 0:
        cnt += 1
        print(subset)

print(cnt)

# 다른 풀이 : 부분집합의 원소의 합이 3이며 길이도 3이 되는 경우, 해당 부분집합을 모두 출력
arr1 = [-2, -1, 0, 1, 2, 3, 4, 5]
arrays =[]
for i in range(1 << len(arr1)):  # 0 ~ (2 ^ n - 1)
    arr = []
    for j in range(len(arr1)):
        if i & (1 << j):
            arr.append(arr1[j])
    arrays.append(arr)
    # print(bin(i), arr)

# print(arrays)
result = [i for i in arrays if sum(i) == 3 and len(i) == 3]
print(*result, sep='\n')

