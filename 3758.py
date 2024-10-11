from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    # 팀 개수, 문제의 개수, 나의 팀 아이디, 로그의 길이
    n, k, my_team, m = map(int, input().split())
    log_table = defaultdict(lambda: [[0]*(k+1), 0, 0])
    for i in range(1, m + 1): # 로그를 통해 정보 수집
        t, p, s = map(int, input().split()) # 팀 아이디, 문제 번호, 점수
        # 문제별 점수 갱신 : log_table[t][0][p] = max(log_table[t][0][p], s)
        log_table[t][0][p] = max(log_table[t][0][p], s)
        # 마지막 제출 시각 갱신 : log_table[t][1] = i
        log_table[t][1] = i
        # 총 제출횟수 갱신 :
        log_table[t][2] += 1

    # 순위 매기기
    rank = []
    for key, val in log_table.items():
        data = (key, sum(val[0]), -val[2], -val[1])
        rank.append(data)
    rank.sort(key= lambda x: (x[1], x[2], x[3]), reverse=True) # 내림차순
    # print(rank)
    for i in range(n):
        if rank[i][0] == my_team:
            print(i + 1)


