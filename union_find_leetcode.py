class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def find(n, par):
            if par[n] == n:
                return n
            else:
                par[n] = find(par[n], par)
            return par[n]

        def union(p, q, par):  # 사이클 확인용
            if par[find(p, par)] > par[find(q, par)]:
                a, b = q, p
            else:
                a, b = p, q
            if find(a, par) != find(b, par):
                par[find(b, par)] = find(a, par)  # 숫자가 작을수록 순위가 높음
                # print(a, b, "union")
                # print(find(b, par))
            else:  # 사이클이 존재하는 경우
                return

        def connected(p, q, par):
            return find(p, par) == find(q, par)

        edges.sort(reverse=True)
        par_a = [i for i in range(n + 1)]  # 처음에 모든 노드의 부모노드는 자기 자신
        par_b = [i for i in range(n + 1)]
        adj_a = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        adj_b = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        global cnt_r, cnt_g
        cnt_r = cnt_g = 0  # 색깔별로 지울 수 있는 간선의 수
        edge_a = []  # 앨리스 기준 없애도 되는 파란 간선
        edge_b = []  # 밥 기준 없애도 되는 파란 간선
        visited_a = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        visited_b = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        # 인접배열로 접근
        for edge in edges:
            color, n1, n2 = edge[0], edge[1], edge[2]
            if color == 1 or color == 3:
                if adj_a[n1][n2]:
                    cnt_r += 1
                    # print("remove duplicate", cnt_r)
                adj_a[n1][n2] = adj_a[n2][n1] = color
            if color == 2 or color == 3:
                if adj_b[n1][n2]:
                    cnt_g += 1
                adj_b[n1][n2] = adj_b[n2][n1] = color

        # print(adj_a, adj_b)
        # dfs 실시
        def dfs(i, person, adj_m, par, edge, visited):  # 시작 노드가 i
            global cnt_r, cnt_g
            for j in range(1, n + 1):
                # print([i, j])
                if adj_m[i][j] == 0 or visited[i][j] or visited[j][i]:
                    continue
                visited[i][j] = visited[j][i] = 1
                if connected(i, j, par):  # 사이클 발생
                    # print("cycle", [i, j])
                    if adj_m[i][j] == 3:  # 사이클 발생 간선이 파란색이면
                        edge.append([i, j])
                    else:
                        if person:
                            cnt_g += 1
                        else:
                            cnt_r += 1

                else:  # 아직 방문하지 않은 노드라면
                    union(i, j, par)  # 연결해주고
                    dfs(j, person, adj_m, par, edge, visited)  # 해당 지점에서 다시 탐색하기

        dfs(1, 0, adj_a, par_a, edge_a, visited_a)
        # print("done")
        dfs(1, 1, adj_b, par_b, edge_b, visited_b)

        # 모든 노드를 탐색 가능한지 확인
        print(par_a, par_b, edge_a, edge_b)
        if len(set(par_a)) != 2 or len(set(par_b)) != 2:
            return -1

            # 탐색 가능하다면 파란 간선의 중복여부 확인
        set_a = set(tuple(edge) for edge in edge_a)
        set_b = set(tuple(edge) for edge in edge_b)
        cnt_b = len(set_a & set_b)
        res = cnt_r + cnt_b + cnt_g
        print(cnt_r, cnt_b, cnt_g)
        return res


##############

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        alice = UnionFind(n)
        bob = UnionFind(n)
        edges.sort(reverse=True)  # 타입 3 간선을 먼저 처리하기 위해 정렬

        removed_edges = 0
        for t, u, v in edges:
            u, v = u - 1, v - 1  # 0-based indexing
            if t == 3:
                added_alice = alice.union(u, v)
                added_bob = bob.union(u, v)
                if not added_alice and not added_bob:
                    removed_edges += 1
            elif t == 1:
                if not alice.union(u, v):
                    removed_edges += 1
            else:  # t == 2
                if not bob.union(u, v):
                    removed_edges += 1

        if alice.count != 1 or bob.count != 1:
            return -1

        return removed_edges