#Trie 사용할 수도 있음 - 3043
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # arr1의 모든 prefix 구하기(중복 제거)
        arr1_set = set()
        for e in arr1:
            s = str(e)
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in arr1_set:
                    continue
                arr1_set.add(prefix)
        # print(arr1_set)
        MAX_LEN = 0
        for e in arr2:
            s = str(e)
            for i in range(len(s), 0, -1):  # 길이가 i인 prefix.
                prefix = s[:i]
                if prefix in arr1_set:
                    MAX_LEN = max(MAX_LEN, i)
                    break

        return MAX_LEN
