numbers = [17, 3, 7, 1, 11, 30, 21, 0]

counts = [0] * (max(numbers) + 1)
temp = [0] * len(numbers)

# 각 정수의 개수를 카운트
for i in numbers:
    counts[i] += 1

# 정렬을 위해 카운트 배열을 누적합 배열로 변환(주의할 점은 배열의 가장 큰 정수의 값만큼 반복해야한다는 것)
for i in range(1, max(numbers) + 1):
    counts[i] = counts[i - 1] + counts[i]

# 정렬이 필요한 배열의 가장 뒤에서부터 순차적으로 카운트 배열을 참고하여 정렬
for i in range(len(numbers) - 1, -1, -1):
    counts[numbers[i]] -= 1
    temp[counts[numbers[i]]] = numbers[i]

print(temp)



