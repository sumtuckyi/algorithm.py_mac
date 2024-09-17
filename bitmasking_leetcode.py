# 비트마스킹 이용하여 효율적으로 문자열 탐색하기- 1371
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            print(i, s[i], prefixXOR)
            if mp[prefixXOR] == -1 and prefixXOR != 0: # prefixXOR값이 처음 등장한 인덱스를 저장, 단 0인 경우는 기록할 필요 없음
                mp[prefixXOR] = i
            # prefixXOR 값이 동일한 두 구간 사이의 부분 문자열은 모음의 등장 횟수가 모두 짝수
            # i - mp[prefixXOR]가 모음의 등장 횟수가 모두 짝수인 구간의 길이를 나타냄
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
            print(longestSubstring)

        return longestSubstring