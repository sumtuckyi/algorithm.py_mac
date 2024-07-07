class DifferenceArray:
    def __init__(self, arr):
        self.diff = [0] * (len(arr) + 1)
        self.diff[0] = arr[0]
        for i in range(1, len(arr)):
            self.diff[i] = arr[i] - arr[i - 1]

    def update(self, left, right, value):
        """범위 [left, right]에 value를 더함"""
        self.diff[left] += value
        self.diff[right + 1] -= value

    def get_result(self):
        """원래 배열의 최종 상태를 반환"""
        result = [0] * (len(self.diff) - 1)
        result[0] = self.diff[0]
        for i in range(1, len(result)):
            result[i] = result[i - 1] + self.diff[i]
        return result


# 사용 예시
original = [1, 2, 3, 4, 5]
diff_array = DifferenceArray(original)

# 범위 업데이트 수행
diff_array.update(1, 3, 2)  # 인덱스 1부터 3까지 2를 더함
diff_array.update(2, 4, 3)  # 인덱스 2부터 4까지 3을 더함

# 최종 결과 얻기
result = diff_array.get_result()
print(result)  # 출력: [1, 4, 8, 9, 8]