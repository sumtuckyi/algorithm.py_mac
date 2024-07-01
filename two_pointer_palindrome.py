class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        res = ""
        max_len = 0

        def is_palindrome(start, end):  # 투포인터 이용 - O(N)
            l, r = start, end - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        # 완전탐색을 하여 가능한 모든 부분 문자열을 탐색하되, 팰린드롬 여부 확인을 투 포인터를 이용하여 수행
        for length in range(len(s), 0, -1):  # 부분 문자열의 길이 - 긴 것부터 고려
            for start in range(
                    len(s) - length + 1):  # 부분 문자열의 시작 인덱스(0부터), len이 작아질수록 될 수 있는 시작 인덱스의 수는 많아짐
                if is_palindrome(start, start + length):
                    return s[start:start + length]
        return ""

    # dp 풀이
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = [0, 0]  # 가장 긴 팰린드롬의 시작, 끝 인덱스, 초기값은 한 자리 부분문자열(=첫번째 인덱스 문자열)

        # 길이 1인 팰린드롬 체크
        for i in range(n):  # 총 n개
            dp[i][i] = True

        # 길이 2인 팰린드롬 체크
        for i in range(n - 1):  # 총 n-1개의 길이가 2인 문자열을 모두 확인
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # 길이 3(diff=2)부터 n(diff=n-1)인 부분 문자열 체크
        for diff in range(2, n):  # 각 길이에 대해
            for i in range(n - diff):  # n-diff개의 문자열이 존재 - 시작 인덱스를 i로
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    ans = [i, i + diff]

        return s[ans[0]:ans[1] + 1]



