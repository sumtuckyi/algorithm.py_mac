T = int(input())

def find_all_ancestors(x, arr):
    n = x
    while n != 0:
        arr.append(n)
        n = par[n]

def dfs(top):
    for i in range(len(child_list[top])):
        dfs(child_list[top][i])
        memo[top] += memo[child_list[top][i]]

for tc in range(1, T + 1):
    V, E, first, second = map(int, input().split()) # 정점의 개수, 간선의 개수, 정점 번호 두 개
    par = [0 for _ in range(V + 1)]
    child_list = [[] for _ in range(V + 1)]
    memo = [1 for _ in range(V + 1)]

    # 트리 구현하기
    nodes = list(map(int, input().split()))
    for i in range(E):
        p, c = nodes[i * 2], nodes[i * 2 + 1]
        par[c] = p
        child_list[p].append(c)

    # 공통 조상찾기
    ancestor_first = []
    ancestor_second = []
    find_all_ancestors(first, ancestor_first)
    find_all_ancestors(second, ancestor_second)
    idx_first = len(ancestor_first) - 1
    idx_second = len(ancestor_second) - 1
    cross = 0
    while True:
        if ancestor_first[idx_first] == ancestor_second[idx_second]:
            cross = ancestor_first[idx_first]
            idx_first -= 1
            idx_second -= 1
        else:
            break

    # 서브트리의 크기 구하기
    dfs(cross)

    print(f'#{tc}', cross, memo[cross])




