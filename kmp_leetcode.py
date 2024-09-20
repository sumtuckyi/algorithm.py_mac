# 주어진 문자열의 앞에 문자를 덧붙여서 만들 수 있는 최단 길이의 회문 구하기 - 214
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_s = s[::-1]
        new_s = s + '#' + reversed_s

        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(new_s)
        chars_to_add = reversed_s[:len(s) - lps[-1]]

        return chars_to_add + s