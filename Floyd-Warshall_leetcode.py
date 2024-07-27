# n개의 출발점-(n-1)개의 도착점 간의 최단거리를 계산 - 1334번
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        INF = float('inf')
        reachable = [0] * n  # 도달가능한 도시의 수
        graph = [[INF] * n for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0

        # 그래프 생성
        for s, e, d in edges:
            graph[s][e] = graph[e][s] = d  # 양방향으로 탐색 가능

        # 플로이드-워셜 알고리즘
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        min_reachable = n
        res = -1

        for i in range(n):
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    reachable[i] += 1

        for idx, cities in enumerate(reachable):
            if cities <= min_reachable:
                min_reachable = cities
                res = idx
        return res
