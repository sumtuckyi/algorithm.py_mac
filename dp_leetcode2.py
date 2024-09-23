# 2707 - bottom up dp
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0]*(n + 1)

        for start in range(n - 1, -1, -1): # (n-1)에서 시작하는 경우부터 0에서 시작하는 경우까지
            dp[start] = dp[start + 1] + 1 # 사용할 수 있는 문자가 하나 더 늘었으므로 일단 +1
            for end in range(start, n):
                cur = s[start:end + 1] # end 인덱스까지의 문자를 사용했을 때 만들어지는 부분 문자열
                if cur in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1]) # end 인덱스까지의 문자를 사용해서 단어를 만들었으므로 그 다음 인덱스의 문자부터 사용할 수 있는 경우와 같아진다. 따라서 dp[end + 1]과 비교
        print(dp)
        return dp[0]