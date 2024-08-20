# 게임이론의 균형 찾기 + dp - 1140번
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # Prefix sums to quickly calculate the sum of any subarray
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                # Try taking X piles where X ranges from 1 to 2 * m
                max_take = 2 * m
                for X in range(1, max_take + 1):
                    if i + X <= n:  # (n-i)개가 남았을 때, X개를 선택할 수 있다면
                        # suffix_sum[i] - dp[i + X][max(m, X)]는 상대방이 가져갈 수 있는 최대 돌의 수
                        # 내가 X개의 돌더미를 선택했을 때, 이후에 상대방의 차례에서 i+X번째 돌더미부터 남아있을 것이고
                        # m = max(m,X)일 것이다.
                        # 이때 남은 돌더미 중에 최대로 얻을 수 있는 값이 dp[i + X][max(m, X)]이다.
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + X][max(m, X)])

        # The result for the first player with the entire piles and m = 1
        print(dp)
        return dp[0][1]

