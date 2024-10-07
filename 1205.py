import bisect
from bisect import bisect_left
from collections import defaultdict

N, t, P = map(int, input().split())
# 리스트에 있는 점수의 개수(rank의 길이), 새 점수, 리스트 최대 길이

if N == 0: # 현재 랭킹 리스트가 비어있는 경우
    print(1)
    exit()
else:
    rank = list(map(int, input().split()))
    answer = 0
    # 동일한 점수가 몇 개인지도 중요
    score_table = defaultdict(int)
    for score in rank:
        score_table[score] += 1

    rank = sorted(set(rank), reverse=True)

    # 새 점수가 몇 등인지 구하기
    nxt_rank = 1  # 1로 초기화
    cnt = 0 # 리스트에 들어있는 점수의 개수
    tof = False
    for i in rank:
        if i > t:
            nxt_rank += score_table[i]
            cnt += score_table[i]
            if cnt >= P:  # 아직 새 점수가 나오지도 않았는데 이미 랭킹 리스트가 꽉 찬 경우
                answer = -1
                break
        elif i == t:
            same_score = score_table[i]  # 새 점수와 같은 점수가 몇 개인지 확인
            if cnt + same_score + 1 > P:  # 새 점수는 랭킹에 진입 못 함
                answer = -1
            else: # P보다 같거나 작다면
                answer = nxt_rank
            tof = True
            break
        else: # 새 점수보다 작은 경우
            if cnt < P:
                answer = nxt_rank
                tof = True
                break
    # 랭킹 리스트를 다 돌았는데 아직 비었을 때
    if cnt < P and not tof:
        answer = nxt_rank
    print(answer)


