# 내장함수 대신 merge_sort 구현하기 - 912
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge_sort(arr):
            # base case: if the array is already sorted (length is 1 or less), return it
            if len(arr) <= 1:
                return arr

            # find the middle point to divide the array into two halves
            mid = len(arr) // 2

            # recursively sort both halves
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])

            # merge the sorted halves
            return merge(left_half, right_half)

        def merge(left, right):
            # left와 right는 이미 정렬된 상태
            sorted_array = []  # 두 배열을 정렬하여 합친 배열
            i = j = 0  # 각 배열에서 비교할 요소의 index

            # compare each element of the two halves and append the smaller one to the sorted array
            while i < len(left) and j < len(right):  # 두 배열 모두에 요소가 남아있다면
                # 더 작은 값을 먼저 배열에 추가
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1

            # if there are remaining elements in the left half, append them
            # 왼쪽배열에만 요소가 남은 경우 모두 추가
            while i < len(left):
                sorted_array.append(left[i])
                i += 1

            # if there are remaining elements in the right half, append them
            # 마찬가지로 오른쪽배열에만 요소가 남은 경우 모두 추가
            while j < len(right):
                sorted_array.append(right[j])
                j += 1

            return sorted_array

        return merge_sort(nums)

