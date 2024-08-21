# 특수한 프린터로 문자열을 출력하는 최적의 방법 / dp (bottom up) - 664
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp[i][j] : 부분 문자열 s[i:j+1]를 프린트하는데 필요한 최소 turns
        # 부분문자열의 길이가 1인 경우를 채운다.
        for i in range(n):
            dp[i][i] = 1
        # 부분 문자열의 길이를 2에서 n으로 늘려가며 dp배열 채우기
        # 길이가 l일 때, 부분 문자열의 start 인덱스는 0에서 (n-l+1)까지
        # end 인덱스는 (start+l-1)이 된다.
        # 최악의 경우를 상정하여 dp배열의 나머지 부분을 채운다.
        for l in range(2, n + 1):  # 부분 문자열의 길이가 l일 때
            for start in range(0, n - l + 1):  # 가능한 시작 인덱스에 대해
                end = start + l - 1
                dp[start][end] = l  # 종료 인덱스는 s+l-1로 결정됨
                # split은 현재 부분문자열을 또 다시 나누는 위치
                for split in range(l - 1):  # 부분 문자열의 길이가 2이면 1회 나눌 수 있고, l이면 l-1회 나눌 수 있다.
                    total = dp[start][start + split] + dp[start + split + 1][end]
                    if s[start + split] == s[end]:
                        total -= 1
                    dp[start][end] = min(dp[start][end], total)

        return dp[0][n - 1]
