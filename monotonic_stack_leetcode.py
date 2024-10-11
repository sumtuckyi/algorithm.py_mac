# 단조 스택 사용하기 - 962
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices_stack = []
        max_width = 0

        # indices_stack 채우기 - 위로 갈수록 큰 값의 인덱스가 쌓인다.
        for i in range(n):
            if indices_stack and nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)
            if not indices_stack:
                indices_stack.append(i)

        # nums 배열을 뒤에서부터 순회한다.
        for i in range(n - 1, -1, -1):  # n-1에서 0까지 순회
            while indices_stack and nums[indices_stack[-1]] <= nums[i]:  # indices_stack 최상단 인덱스에 위치한 값보다 현재 값이 크면
                max_width = max(max_width, i - indices_stack[-1])  # 최댓값을 갱신하고,
                indices_stack.pop()  # indices_stack의 최상단 값을 삭제

        return max_width
    # 투포인터 사용
    def maxWidthRamp2(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        # i번 인덱스의 오른쪽에 있는 요소이면서 nums[i]보다 큰 수 중에 가장 큰 수
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        # 투 포인터 모두 인덱스 0에서 시작
        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            # right인덱스의 right_max값이 nums[left]보다 작아지는 순간 left 인덱스를 오른쪽으로 한 칸 이동
            while left < right and nums[left] > right_max[right]:
                left += 1
            # left 인덱스가 움직이지 않는 동안 right 인덱스는 오른쪽으로 계속 이동, 1칸 씩 이동할 때마다
            # max_width를 계산
            max_width = max(max_width, right - left)
            right += 1

        return max_width


