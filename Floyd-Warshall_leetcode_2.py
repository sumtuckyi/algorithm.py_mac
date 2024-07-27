# 알파벳을 노드라고 생각하면 다중 시작 노드에서 다중 도착 노드까지의 최소비용을 구하는 문제로 치환 가능 - 2976
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = 10 ** 9
        cost_mat = [[INF] * 26 for _ in range(26)]  # dp 배열
        res = 0
        # a(97) ~ z(122)

        for i in range(26):
            cost_mat[i][i] = 0

        for i in range(len(cost)):
            f, t = ord(original[i]) - ord('a'), ord(changed[i]) - ord('a')
            cost_mat[f][t] = min(cost[i], cost_mat[f][t])  # 단방향 그래프

        # dp 배열 채우기
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    cost_mat[i][j] = min(cost_mat[i][j], cost_mat[i][k] + cost_mat[k][j])

        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            else:
                f, t = ord(source[i]) - ord('a'), ord(target[i]) - ord('a')
                if cost_mat[f][t] == INF:  # 시작점과 끝점이 연결되어 있지 않다면
                    return -1
                res += cost_mat[f][t]

        return res