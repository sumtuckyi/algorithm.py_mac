# 10만개의 배열을 탐색, 서로 다른 두 배열에서 나온 값의 차이 중 최댓값을 찾기 - 그리디 624
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        m = len(arrays)
        res = 0
        min_val, max_val = arrays[0][0], arrays[0][-1]
        for i in range(1, m):
            # 모든 배열의 최솟값과 최댓값을 한 번씩은 탐색
            nxt_min = arrays[i][0]
            nxt_max = arrays[i][-1]
            # 이전 배열의 최댓값과 지금 배열의 최솟값의 차이, 이전 배열의 최솟값과 지금 배열의 최댓값의 차이를 모두 고려
            res = max(res, abs(max_val - nxt_min), abs(min_val - nxt_max))

            # 지금껏 나온 최솟값 중 최솟값을, 지금껏 나온 최댓값 중 최댓값을 갱신 -> 이렇게 하더라도 같은 배열에서 나온 두 요소의 차이를 계산하는 일은 없음, 왜냐하면 res 계산 시에는 늘 다른 배열에서 나온 값 사이의 차이를 계산하기 때문
            min_val = min(min_val, nxt_min)
            max_val = max(max_val, nxt_max)
        return res

