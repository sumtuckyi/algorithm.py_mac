#한 팀은 6인의 선수로 구성, 개인의 성적으로 팀 성적을 계산
# 팀 내 상위 4인의 점수를 합하여 계산(낮을수록 좋음)
# 다만, 팀 선수가 6인이 되지 않는 경우 제외, 동점인 경우 5번째로 들어온 선수의 점수를 고려
# 우승팀을 출력한다.
# 팀은 최대 200개
# 팀 구성 조건을 충족하지 못한 팀의 팀원은 아예 점수를 얻지 못한다. 이를 제외하고 점수를 매긴다.
T = int(input())


for _ in range(T):
    N = int(input()) # 참가한 선수의 수
    teams = list(map(int, input().split()))
    cnt_teams = [0] * 201
    for t in teams:
        cnt_teams[t] += 1

    disqualified = set() # 실격된 팀
    for i in range(201):
        if cnt_teams[i] < 6:
            disqualified.add(i)

    scores = [[] for _ in range(201)]
    score = 1
    for i in range(N):
        if teams[i] in disqualified:
            continue
        scores[teams[i]].append(score)
        score += 1

    # 우승팀 찾기
    MIN_SCORE = 1e15
    ans = 0
    fifth = 0
    for i in range(201): # i는 팀번호
        if len(scores[i]) == 0:
            continue
        total_score = sum(scores[i][:4])
        if total_score < MIN_SCORE:
            MIN_SCORE = total_score
            ans = i
            fifth = scores[i][4]
        elif total_score == MIN_SCORE: # 동점팀이 나타나면
            if fifth > scores[i][4]: # 비교해서
                ans = i # 갱신
                fifth = scores[i][4]
    # print(scores[:4])
    print(ans)



