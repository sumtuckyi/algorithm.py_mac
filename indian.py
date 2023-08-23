from collections import defaultdict


def find(n):
    if par[n] == n:
        return n
    else:
        par[n] = find(par[n])
    return par[n]


def union(a, b):
    if find(a) != find(b):  # 같은 팀이 아닌 경우
        if rank[find(a)] > rank[find(b)]:
            par[find(b)] = find(a)  # 랭크가 낮은 루트를 가진 트리가 자식으로 들어감
        else:
            par[find(a)] = find(b)
            if rank[find(a)] == rank[find(b)]:
                rank[find(b)] += 1
    else:  # 이미 같은 팀인 경우
        return


N = int(input())  # 명령의 수
par = {chr(i): chr(i) for i in range(65, 90 + 1)}  # 루트 노드를 저장
rank = {chr(i) : i for i in range(65, 90 + 1)}  # 앞순서의 알파벳일수록 랭크가 낮음
for _ in range(N):
    n1, n2 = input().split()  # 서로 다른 그룹일 경우 합칠 두 노드
    union(n1, n2)


# 조직된 팀의 개수 구하기
cnt = 0  # 조직된 팀의 개수
g = 0  # 개인연주자를 포함한 그룹의 수
new = defaultdict(int)
for value in par.values():
    new[find(value)] += 1
for value in new.values():  # 집합의 크기가 1보다 큰 경우를 카운트(개인연주자가 아닌 경우)
    if value > 1:
        cnt += 1
for key, value in par.items(): # 개인연주자 + 단체의 수
    if key == value:
        g += 1
print(cnt)  # 집단의 수
print(g - cnt)  # 개인연주자의 수
