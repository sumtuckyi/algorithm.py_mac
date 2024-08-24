# 정규 표현식 이용해서 문자열 파싱 + 통분하기 - 592
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0 # 분자
        denom = 1 # 분모

        # separate expression into signed numbers
        # 문자열을 / 또는 +, - 기호의 위치에서 분리
        nums = re.split("/|(?=[-+])", expression) # '/'를 기준으로 나누되, '+','-'가 나오면 그 앞에서 나눈다.
        nums = list(filter(None, nums))
        # print(nums)

        for i in range(0, len(nums), 2): # 짝수 인덱스에만 접근
            curr_num = int(nums[i]) # 현재 분자
            curr_denom = int(nums[i + 1]) # 현재 분모
            print(curr_num, curr_denom)

            num = num * curr_denom + curr_num * denom # 분자 계산
            denom = denom * curr_denom # 분모 계산

        # 연속해서 통분하여 계산한 값을 기약분수로 표기
        gcd = abs(self._find_gcd(num, denom)) # 분자와 분모의 최대공약수

        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)