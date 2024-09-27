# 1번 노드를 루트로 하는 양방향 그래프 - 이진 트리라는 보장 없음
# 인접 배열로 그래프 구현
# 노드의 수는 최대 30만
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

ans = 0
adj_list = [[] for _ in range(N + 1)]
# 1번 노드로부터의 거리 저장
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)


MAX_DEPTH = 17
subtree_node = [1]*(N + 1)

def dfs(node, par):
    for child in adj_list[node]:
        if child != par: # 양방향이므로 거슬러 올라가는 방향의 탐색은 걸러준다.
            subtree_node[node] += dfs(child, node)
    return subtree_node[node]

dfs(1, -1)
# ans는 각 간선의 사용횟수의 총합
# 다양성의 합 계산하기 - 간선을 기준으로 하며, 모든 간선을 고려한다.
for i in range(2, N + 1): # (N-1)개의 간선
    not_used = N - subtree_node[i] # 전체 노드 중 i번 노드의 서브트리에 포함되어 있지 않은 노드의 수
    ans += (N*(N-1)//2) - (not_used*(not_used - 1)//2)
print(ans)

