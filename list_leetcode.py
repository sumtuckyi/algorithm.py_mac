# 1380 - list comprehension

class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # n = len(matrix)
        # m = len(matrix[0])
        # res = []
        # for i in range(n):
        #     num = None
        #     min_idx = 0
        #     # i번째 행에서 가장 작은 수의 인덱스 찾기
        #     for j in range(m):
        #         if matrix[i][j] <= matrix[i][min_idx] :
        #             min_idx = j
        #             num = matrix[i][j]
        #     # print(num)
        #     # min_idx열에서 가장 큰 수인지 판별하기
        #     max_idx = i #현재 기준 행
        #     for k in range(n):
        #         if matrix[k][min_idx] > matrix[i][min_idx]: # i행에서의 최솟값이 j열에서 최댓값이 아니면 중단
        #             num = None
        #             break
        #     if num is not None:
        #         res.append(num)
        # return res

        n, m = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]

        return [num for num in row_min if num in col_max]




