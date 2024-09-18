# sort()의 key인자로 함수 전달하여 원하는대로 정렬하기 - 179
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(num1, num2):
            if str(num1) + str(num2) > str(num2) + str(num1):
                return -1  # num1을 먼저 배치
            else:
                return 1  # num2를 먼저 배치

        table = defaultdict(list)
        for num in nums:
            first_digit = str(num)[0]
            table[first_digit].append(num)

        for key in table:
            table[key].sort(key=cmp_to_key(compare))
        # print(table)

        res = ""
        for i in sorted(table.keys(), reverse=True):
            arr = table[i]
            for a in arr:
                res += str(a)
                if res == "0":
                    return "0"

        # print(res)

        return res