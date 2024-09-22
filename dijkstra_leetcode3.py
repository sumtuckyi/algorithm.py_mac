# 간선의 가중치를 변경하여 목표 비용에 도달하기 - 다익스트라 알고리즘 2699
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:

        # 인접 리스트
        graph = [[] for _ in range(n + 1)]
        INF = 2e9

        for edge in edges:
            n1, n2, w = edge[0], edge[1], edge[2]
            if w == -1:
                continue
            graph[n1].append((n2, w))
            graph[n2].append((n1, w))

        shortest_path = self._dijkstra(graph, source, destination)
        # 최단 경로가 target과 일치하는 경우 - edges에서 가중치가 -1인 간선만 바꾼다.
        if shortest_path == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        if shortest_path < target:
            return []

        # shortest_path > target인 경우 -1인 간선을 추가해본다.
        # 그래프에 가중치가 -1인 간선을 하나씩 추가하면서 최단 경로를 갱신
        for idx, (n1, n2, w) in enumerate(edges):
            if w == -1:
                edges[idx][2] = 1
                graph[n1].append((n2, 1))
                graph[n2].append((n1, 1))

                new_path = self._dijkstra(graph, source, destination)
                if new_path <= target:
                    edges[idx][2] += (target - new_path)  # 기존값에 부족한 부분만 더한다.

                    for i in range(idx + 1, len(edges)):  # 나머지 가중치가 -1인 간선의 가중치를 아예 큰 값으로 바꾼다.
                        if edges[i][2] != -1:
                            continue
                        edges[i][2] = INF
                    return edges
        return []

    def _dijkstra(self, graph, source, dest):
        pq = [(0, source)]  # 나중에 heappop으로 인해 최소힙으로 변환된다.
        dist = [float('inf')] * (len(graph))
        dist[source] = 0

        while pq:
            w, cur = heapq.heappop(pq)

            if dist[cur] < w:
                continue

            for nxt, nxt_w in graph[cur]:
                if dist[nxt] <= w + nxt_w:
                    continue
                heapq.heappush(pq, (w + nxt_w, nxt))
                dist[nxt] = w + nxt_w

        return dist[dest]




