from itertools import combinations


def possible(v, group):  # 그룹의 연결여부 판단
    visited = [0]*(N+1)
    q = [v]
    visited[v] = 1
    while q:
        start = q.pop()  # deque를 import해서 leftpop()사용할 것
        for n in group:
            if adj_m[start][n] == 1 and visited[n] == 0:
                q.append(n)
                visited[n] = 1
    if visited.count(i) == len(group):
        return True
    return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 마을의 수
    adj_m = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))  # 마을별 유권자의 수
    answer = []
    for i in range(1, N//2 + 1):  # 2개의 권역으로 나누는 모든 경우의 수 탐색
        comb_generator = combinations([i for _ in range(1, N+1)], i)
        for com in comb_generator:
            g1 = list(com)
            g2 = list(set([i for _ in range(1, N+1)]) - set(g1))
            if possible(g1[0], g1) and possible(g2[0], g2):  # 두 권역 모두 각각 연결되어 있다면
                re1 = re2 = 0
                for a in g1:  # 1권역의 유권자 수 계산
                    re1 += voters[a-1]
                for b in g2:  # 2권역의 유권자 수 계산
                    re2 += voters[b-1]
                answer.append(abs(re1-re2))  # 각 경우의 두 권역간 유권자수 차이를 저장
    print(f'#{tc} {min(answer)}')