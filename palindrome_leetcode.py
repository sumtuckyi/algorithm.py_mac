# 가장 가까운 palindrome 찾기 - 564문
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        N = len(n)

        if int(n) <= 10:  # 한자리 수인 경우
            return str(int(n) - 1)
        if int(n) == 11:
            return '9'

        def get_palindrome(n):  # n보다 크면서 가장 작은 팰린드롬 구하기
            s = n[:N // 2]
            s_reversed = s[::-1]
            if N % 2 == 0:  # N의 길이가 짝수인 경우
                if int(s_reversed) > int(n[N // 2:]):  # 문자열의 앞부분을 뒤집은 수가 나머지 반보다 크다면
                    return s + s_reversed
                else:
                    # 문자열의 앞부분에 1을 더했을 때 자릿수가 바뀌는 경우,
                    pl = str(int(s) + 1)
                    if len(pl) > len(s):
                        return pl + pl[:N // 2][::-1]
                    else:
                        return pl + pl[::-1]
            else:  # N의 길이가 홀수인 경우
                if int(s_reversed) > int(n[N // 2 + 1:]):
                    return n[:N // 2 + 1] + s_reversed
                else:
                    temp = str(int(n[:N // 2 + 1]) + 1)
                    temp_reversed = temp[:N // 2][::-1]
                    return temp + temp_reversed

        def get_smaller_palindrome(n):
            s = n[:N // 2]  # 문자열의 앞부분 절반
            s_reversed = s[::-1]
            if N % 2 == 0:  # N의 길이가 짝수인 경우
                if int(s_reversed) < int(n[N // 2:]):  # 문자열의 앞부분을 뒤집은 수가 나머지 반보다 작다면
                    return s + s_reversed
                else:  # 나머지 반보다 크거나 같다면
                    half = str(int(s) - 1)
                    half_reversed = half[::-1]

                    # pl = str(int(s) + 1)
                    if len(half) < len(s):  # 자릿수가 바뀌는 경우 - 무조건 9로만 이루어짐
                        return '9' * (len(s) * 2 - 1)
                    else:
                        return half + half_reversed
            else:  # N의 길이가 홀수인 경우
                if int(s_reversed) < int(n[N // 2 + 1:]):  # 뒤집은 수가 나머지 반보다 작다면
                    return n[:N // 2 + 1] + s_reversed
                else:  # 크다면
                    temp = str(int(n[:N // 2 + 1]) - 1)
                    temp_reversed = temp[: N // 2][::-1]
                    return temp + temp_reversed

        bigger = get_palindrome(n)
        smaller = get_smaller_palindrome(n)
        if abs(int(n) - int(bigger)) < abs(int(n) - int(smaller)):
            return bigger
        else:
            return smaller


