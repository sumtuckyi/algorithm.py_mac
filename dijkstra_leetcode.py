# 2번째 최소비용 경로를 구해야 하는 문제, dist배열을 하나 더 만들어서 해당 노드까지 두 번째로 많이 걸리는 시간을 함께 저장한다 - 2045
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        adj_list = [[] for _ in range(n + 1)]
        # 인접 리스트 생성
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        dist1 = [float('inf') for _ in range(n + 1)]  # node 1에서 idx 노드까지의 최단 거리
        dist2 = [float('inf') for _ in range(n + 1)]  # node 1에서 idx 노드까지의 두 번째 최단 거리

        freq = [0 for _ in range(n + 1)]  # pq에서 반환될 때마다 카운트 - 최대 2번까지 가능
        pq = []

        def dijkstra():
            dist1[1] = 0
            heapq.heappush(pq, (0, 1))  # (dist, node)순서

            while pq:
                cur_time, cur_node = heapq.heappop(pq)
                freq[cur_node] += 1

                # 두 번째 최단 경로를 발견한 경우
                if cur_node == n and freq[cur_node] == 2:
                    return cur_time

                # 제약을 고려한 시간 계산
                if (cur_time / change) % 2:
                    cur_time = change * (cur_time / change + 1) + time
                else:
                    cur_time = cur_time + time

                # 아니라면 cur_node의 이웃노드를 방문
                for next_node in adj_list[cur_node]:
                    if freq[next_node] == 2:
                        continue
                    if dist1[next_node] > cur_time:
                        dist2[next_node] = dist1[next_node]
                        dist1[next_node] = cur_time
                        heapq.heappush(pq, (cur_time, next_node))
                    elif dist2[next_node] > cur_time and cur_time != dist1[next_node]:
                        dist2[next_node] = cur_time
                        heapq.heappush(pq, (cur_time, next_node))

        res = dijkstra()

        return res



