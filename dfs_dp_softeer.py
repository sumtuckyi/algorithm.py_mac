#효도 여행
import sys

input = sys.stdin.readline
sys.setrecursionlimit(5000)


# 1번 정점에서 시작, 하향식 단방향
# 도착지는 무조건 리프 노드 중 하나
# 따라서 선택할 수 있는 경로는 리프 노드의 수 만큼이다.
# 각 경로와 주어진 문자열을 비교하여 LCS를 구한다. 이때의 길이가 행복지수이다.


def dfs(node, dep, path):
    global res
    visited.add(node)

    # dep가 1 늘어날 때마다 경로에 새로 추가되는 문자열을 가지고 dp배열 갱신
    for i in range(1, m + 1):
        if dep == 0:
            continue
        if string[i - 1] == path[dep - 1]:
            dp[dep][i] = dp[dep - 1][i - 1] + 1
        else:
            dp[dep][i] = max(dp[dep - 1][i], dp[dep][i - 1])
        res = max(res, dp[dep][i])

    for next_node, token in tree[node]:
        if next_node in visited:
            continue
        dfs(next_node, dep + 1, path + token)


n, m = map(int, input().split())
string = input()
tree = [[] for _ in range(5001)]

dp = [[0] * (m + 1) for _ in range(n + 1)]  # 행은 path의 길이, 즉 dfs의 깊이, 열은 string의 길이
paths = []
visited = set()
res = 0

for _ in range(n - 1):
    q = input().split()
    n1, n2 = int(q[0]), int(q[1])
    token = q[2]
    tree[n1].append((n2, token))
    tree[n2].append((n1, token))

initial_lcs = [0] * (n + 1)
dfs(1, 0, "")

print(res)
