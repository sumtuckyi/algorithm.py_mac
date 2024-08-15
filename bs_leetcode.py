# k번째로 작은 거리를 구할 때, 가능한 거리의 범위에서 이진 탐색으로 수를 고른다음 해당 거리보다 작은 경우가 k-1가지인지 확인한다. - 719
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()  # 오름차순 정렬

        def count_pairs(diff):  # 거리가 diff보다 작거나 같은 경우의 수를 구하기 - 투포인터 사용
            cnt = 0
            l = 0
            for r in range(1, n):  # nums[1]부터 nums[n-1]까지
                while nums[r] - nums[l] > diff:
                    l += 1
                cnt += r - l
            return cnt

        s, e = 0, nums[-1] - nums[0]
        # e는 나올 수 있는 거리의 최댓값
        while s < e: # 루프 종료 시에 s==e
            mid = (s + e) // 2
            if count_pairs(mid) < k:  # 거리가 mid보다 작은 경우의 수가 k보다 작은 경우
                # mid의 값을 키운다.
                s = mid + 1
            else:  # 같거나 크다면
                # mid값이 찾고 있는 값일 가능성이 있다. 따라서 e = mid - 1로 하게 되면 이 mid값을 배제하게 된다.
                e = mid

        return e

nums = [1, 3, 1, 5, 1]
solution = Solution()
print(solution.smallestDistancePair(nums, 2))