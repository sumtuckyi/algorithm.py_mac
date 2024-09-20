# 주어진 문자열의 앞에 문자를 덧붙여서 만들 수 있는 최단 길이의 회문 구하기 - 214
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_s = s[::-1]
        new_s = s + '#' + reversed_s

        def build_lps(pattern):
            lps = [0] * len(pattern) # pattern[:i]에서 접두사-접미사의 최장 길이를 저장
            length = 0  # 이전까지 일치한 접두사-접미사의 길이
            i = 1 # lps[0]은 항상 0이므로 1부터 탐색 시작

            while i < len(pattern):
                if pattern[i] == pattern[length]: # 일치한다면 접두사-접미사의 길이를 늘린다.
                    length += 1
                    lps[i] = length
                    i += 1
                else: # 일치하지 않을 때,
                    if length != 0:
                        length = lps[length - 1] # 이전에 일치한 접두사-접미사 길이의 위치로 돌아가서 비교, i는 그대로
                    else: # 패턴의 맨 앞 문자와 비교 중이었다면
                        lps[i] = 0 # 접두사-접미사는 0인 것임
                        i += 1
            return lps

        lps = build_lps(new_s)
        chars_to_add = reversed_s[:len(s) - lps[-1]]

        return chars_to_add + s