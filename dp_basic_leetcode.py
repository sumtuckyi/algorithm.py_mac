# 조건을 만족하는 문자열을 만들기 위한 개별 문자 삭제 횟수의 최솟값 구하기 - 1653
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        count_b = 0

        for i in range(n):
            if s[i] == 'a':
                dp[i + 1] = min(dp[i] + 1, count_b)
            else:  # 'b'이면
                count_b += 1
                dp[i + 1] = dp[i]

        # print(dp)
        return dp[-1]