# n번째 ugly number 찾기 - 최소힙 이용 264
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = []
        seen_nums = set()
        primes = [2, 3, 5]
        heappush(h, 1)  # 최소힙에 1만 추가
        for i in range(n - 1):  # n-1회 반복
            cur_num = heappop(h)
            for p in primes:
                temp = cur_num * p
                if temp in seen_nums:
                    continue
                seen_nums.add(temp)  # 중복 제거
                heappush(h, temp)  # 최소힙에 추가
        res = heappop(h)
        return res





