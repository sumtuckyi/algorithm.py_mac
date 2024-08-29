# 그래프 탐색 이론으로 치환해서 풀이 - 947
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        n = len(stones)
        adj_list = [[] for _ in range(n)]

        # 인접 리스트로 그래프 연결관계 확인하기
        for i in range(n):  # i가 노드 번호
            r, c = stones[i][0], stones[i][1]
            for j in range(i + 1, n):  # j는 i번 이후의 노드 번호
                if stones[j][0] == r or stones[j][1] == c:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False] * n

        # dfs
        def helper_dfs(node):
            for nxt in adj_list[node]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                helper_dfs(nxt)

        # 그룹 세기
        group = 0
        for i in range(n):
            if visited[i]:
                continue
            helper_dfs(i)
            group += 1

        # print(group)

        return n - group


class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:

        n = len(stones)
        par = [i for i in range(n)]  # 처음에 모든 노드의 부모는 자기 자신
        cnt = [n]  # 그룹에 속하지 않은 노드 초기화 - 처음에는 모든 노드

        # 보조함수 find
        def find(n):
            if par[n] == n:  # 부모노드가 자기 자신인 경우
                return n
            else:  # 다른 부모노드가 있는 경우
                par[n] = find(par[n])  # 부모노드를 찾아 거슬러 올라감 - 부모 노드가 자기 자신인 루트 노드를 만날 때까지
            return par[n]

        # 보조함수 union
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_x == par_y:
                return
            else:
                par[par_y] = par_x  # py를 px의 하위 트리로 연결
                cnt[0] -= 1 # 새로운 연결이 생겼으니 연결되지 않은 노드의 수를 감소시킴

        # union 작업 수행
        for i in range(n):  # i가 노드 번호
            r, c = stones[i][0], stones[i][1]
            for j in range(i + 1, n):  # j는 i번 이후의 노드 번호
                if stones[j][0] == r or stones[j][1] == c:
                    union(i, j)
                    # print(i, j, par)

        return n - cnt[0]
