# 최적화 필요 - 1605
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        r, c = len(rowSum), len(colSum)
        grid = [[None for _ in range(c)] for _ in range(r)]  # 조건을 만족하는 배열

        # 행이나 열의 합이 0이라면 grid를 0으로 채우고 시작
        for i in range(r):
            if rowSum[i] == 0:
                for j in range(c):
                    grid[i][j] = 0
        for i in range(c):
            if colSum[i] == 0:
                for j in range(r):
                    grid[j][i] = 0
        if sum(rowSum) == 0 and sum(colSum) == 0:
            return grid

        while True:
            min_v_r = min(filter(lambda x: x > 0, rowSum))  # 0보다 큰 최솟값 반환
            idx_r = rowSum.index(min_v_r)
            min_v_c = min(filter(lambda x: x > 0, colSum))
            idx_c = colSum.index(min_v_c)
            if min_v_r > min_v_c:  # 행의 값이 더 크면
                grid[idx_r][idx_c] = min_v_c  # 열의 값을 그리드에 지정
                rowSum[idx_r] -= min_v_c  # 해당 행의 남은 값 갱신
                colSum[idx_c] = 0
                for i in range(r):
                    if grid[i][idx_c] == None:
                        grid[i][idx_c] = 0
            else:  # 행의 값이 작거나 같으면
                grid[idx_r][idx_c] = min_v_r  # 행의 값을 그리드에 지정
                rowSum[idx_r] = 0
                colSum[idx_c] -= min_v_r  # 해당 열의 남은 값 갱신
                for i in range(c):
                    if grid[idx_r][i] == None:
                        grid[idx_r][i] = 0
            if sum(rowSum) == 0:  # 그리드를 모두 채운 경우
                break

        return grid