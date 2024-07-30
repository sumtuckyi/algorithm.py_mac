# 2045 - 다익스트라 대신 bfs로 접근(모든 간선의 가중치가 같기 때문에 가능)
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

        dist1 = [-1 for _ in range(n + 1)]  # node 1에서 idx 노드까지의 최단 거리
        dist2 = [-1 for _ in range(n + 1)]  # node 1에서 idx 노드까지의 두 번째 최단 거리

        # freq = [0 for _ in range(n + 1)] # pq에서 반환될 때마다 카운트 - 최대 2번까지 가능
        q = deque()
        q.append((1, 1))  # (node, freq)순으로 관리
        dist1[1] = 0

        while q:
            node, freq = q.popleft()

            cur_time = dist1[node] if freq == 1 else dist2[node]

            # 제약을 고려한 시간 계산
            if (cur_time / change) % 2:
                cur_time = change * (cur_time / change + 1) + time
            else:
                cur_time = cur_time + time

            # 아니라면 cur_node의 이웃노드를 방문
            for next_node in adj_list[node]:
                if dist1[next_node] == -1:  # 첫방문이면
                    dist1[next_node] = cur_time
                    q.append((next_node, 1))
                elif dist2[next_node] == -1 and cur_time != dist1[next_node]:  # 두 번째 방문이면
                    if next_node == n:
                        res = cur_time
                    dist2[next_node] = cur_time  # 두 번째로 짧은 시간을 업데이트
                    q.append((next_node, 2))

        return res



