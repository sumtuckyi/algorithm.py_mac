# 650번 문제
# 백트래킹으로 접근
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 1  # 최초의 문자열 길이
        temp = 0  # 클립보드 문자열(현재 붙여넣기 시에 추가되는 문자열의 길이)
        op = 0  # 동작 횟수
        min_op = [float('inf')]

        def operation(num, temp, op):

            if num == n:
                min_op[0] = min(min_op[0], op)
                return

            if num > n:
                return

            # 이전에 전체복사한 값이 있다면 그 값을 붙여넣기 - 1회 동작 추가
            if temp != 0:
                operation(num + temp, temp, op + 1)
            # 현재 문자열을 전체복사한 다음에 붙여넣기 - 2회 동작 추가

            operation(num * 2, num, op + 2)

        operation(num, temp, op)
        return min_op[0]

# dp로 접근
class Solution2(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        if n == 1:
            return 0

        for i in range(2, n + 1):  # 목표값이 2에서 n인 경우를 모두 탐색
            dp[i] = i  # 길이 1인 문자열을 복사 붙여넣기만 하는 경우
            # i의 모든 약수 탐색
            for j in range(1, i // 2 + 1):
                if i % j == 0:  # j가 i의 약수인 경우
                    dp[i] = dp[j] + (i // j)  # j를 만들고 j값을 복사해서 붙여넣기

        return dp[n]





