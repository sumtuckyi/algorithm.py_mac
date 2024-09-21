# 숫자를 사전순으로 정렬하기 - 386
# str으로 변환한 값을 기준으로 정렬하면 원하는 순서를 쉽게 얻을 수 있다.
# 2번째 접근 : Trie 이용


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        nums = list(range(1, n + 1))
        table = defaultdict(list)
        for num in nums:
            first_digit = str(num)[0]
            table[first_digit].append(num)

        for key in table:
            table[key].sort(key=lambda x: str(x))

        res = []
        for i in sorted(table.keys()):
            arr = table[i]
            for a in arr:
                res.append(a)

        return res