class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        # 가중치 저장
        graph = [[] for _ in range(n)]  # 인접 리스트로 저장
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        # n번 노드까지의 최대 확률
        probability = [float('-inf')] * n

        # 다익스트라 함수로 각 시작점부터 각 노드까지의 최대 확률 구하기
        def dijkstra(start):
            pq = []
            heapq.heappush(pq, (-1, start))  # 최대힙처럼 동작하도록 음수 확률 저장
            probability[start] = 0

            while pq:
                prob, now = heapq.heappop(pq)  # now까지의 성공확률
                prob = -prob  # 다시 양수로

                # 목표 노드에 도착했을 때의 확률이 목표 확률 - 최적화
                if now == end_node:
                    return prob

                if probability[now] > prob:  # 계산되어 있는 최대 확률보다 작다면 패스
                    continue

                for next_node, next_prob in graph[now]:

                    # next_node까지의 새로운 확률 계산
                    temp = math.log(prob) + math.log(next_prob)
                    n_cost = math.exp(temp)

                    if n_cost <= probability[next_node]:
                        continue
                    probability[next_node] = n_cost
                    heapq.heappush(pq, (-n_cost, next_node))

        dijkstra(start_node)
        # print(probability)
        # 도달가능하지 않은 경우
        if probability[end_node] == float('-inf'):
            return 0
        return probability[end_node]