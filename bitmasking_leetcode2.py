class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):  # s는 문자열
            l = len(s)
            num = int(s, 2)  # 문자열을 이진수로 변환
            res = bin(num ^ ((1 << l) - 1))
            return res[2:].zfill(l)

        prev = '0'  # 초항
        nxt = '0'
        for i in range(n - 1):  # n번째 항을 구할 때까지 반복
            nxt = prev + '1' + invert(prev)[::-1]
            prev = nxt

            # print(nxt)

        return nxt[k - 1]