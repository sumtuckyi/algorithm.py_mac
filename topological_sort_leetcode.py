# 조건을 만족하는 행렬을 만드는 문제, 그래프로 치환하여 노드 간 위상정렬을 실시 - 2392
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """

        # 위상정렬 함수
        def top_sort(indegrees, adj_list):
            res = []
            q = deque()

            for i in range(1, k + 1):
                if indegrees[i] == 0:  # 진입차수가 0인 노드이면 - 우선순위가 높은 노드
                    q.append(i)

            while q:
                cur = q.popleft()  # 진입차수가 0이거나 0이된 노드 - 우선순위가 높은 노드가 이미 다 처리됨
                res.append(cur)

                for node in adj_list[cur]:  # 해당노드가 선행되어야 하는 나머지 노드를 순회하며 진입차수를 줄여준다.
                    indegrees[node] -= 1
                    if indegrees[node] == 0:
                        q.append(node)

            if len(res) == k:  # 모든 노드가 우선순위에 따라 정렬되면
                return res
            else:  # 사이클이 존재하면
                return []

        # k개의 노드 존재
        # 인접리스트로 관리
        adj_list_r = [[] for _ in range(k + 1)]
        adj_list_c = [[] for _ in range(k + 1)]

        # 각 노드의 진입차수 저장
        indegrees_r = [0] * (k + 1)
        indegrees_c = [0] * (k + 1)

        # row 조건에서 진입차수 및 연결관계 도출
        for con in rowConditions:
            n1, n2 = con[0], con[1]
            adj_list_r[n1].append(n2)
            indegrees_r[n2] += 1

        # cycle의 존재 확인하기
        sorted_nodes_r = top_sort(indegrees_r, adj_list_r)
        if not sorted_nodes_r:
            return []

        # col 조건을 그래프로 변환
        for con in colConditions:
            n1, n2 = con[0], con[1]
            adj_list_c[n1].append(n2)
            indegrees_c[n2] += 1

        sorted_nodes_c = top_sort(indegrees_c, adj_list_c)
        if not sorted_nodes_c:
            return []

        # 사이클이 존재하지 않는다면 우선순위에 따른 행렬 생성
        matrix = []
        for i in range(k):
            row = []
            for j in range(k):
                if sorted_nodes_r[i] == sorted_nodes_c[j]:
                    row.append(sorted_nodes_r[i])
                else:
                    row.append(0)
            matrix.append(row)
        return matrix
