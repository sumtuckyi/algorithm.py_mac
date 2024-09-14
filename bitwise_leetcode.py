# 누적합 이용, XOR 연산 - 1310
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * len(arr)
        prefix_sum[0] = arr[0]
        for i in range(1, len(arr)):
            prefix_sum[i] = prefix_sum[i - 1] ^ arr[i]

        # print(prefix_sum)
        res = []
        for l, r in queries:
            if l == r:
                res.append(arr[l])
            elif l == 0:
                res.append(prefix_sum[r])
            else:
                res.append(prefix_sum[r] ^ prefix_sum[l - 1])

        return res