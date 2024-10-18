# union-find 기초문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())  # 원소의 개수는 N + 1, 연산의 개수

par = [0]*(N + 1)
rank = [0] * (N + 1)

for i in range(N + 1):  # 0부터 N까지 총 N+1개의 원소가 존재
    par[i] = i  # 처음에 노드 i의 부모는 자기 자신


# find : 해당 노드의 부모 노드를 반환함. 부모노드가 동일 하면 같은 집합임
def find(n):
    while par[n] != n:
        par[n] = par[par[n]]
        n = par[n]
    return n


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        # rank에 따라 트리를 병합
        if rank[root_a] > rank[root_b]:
            par[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            par[root_a] = root_b
        else:
            par[root_b] = root_a
            rank[root_a] += 1


for _ in range(M):
    q, a, b = map(int, input().split())
    if q:  # 1이면 같은 집합인지 확인
        if find(a) != find(b):
            print('no')
        else:
            print('yes')
    else:  # 0이면 합집합 연산
        union(a, b)


