def right(idx, N):  # 해당 인덱스를 기준으로 오른쪽 탐색
    bn = idx+1
    while bn <= N:
        if popped[bn] == 0:
            return scores[bn]
        else:
            bn += 1
    return 0  # 오른쪽에 남은 풍선이 없다면


def left(idx, N):
    bn = idx-1
    while bn >= 1:
        if popped[bn] ==0:
            return scores[bn]
        else:
            bn -= 1
    return 0


def cal_score(lb, rb, num):
    ans = 0
    if rb and lb:  # 인접풍선이 두 개이면
        ans += (rb * lb)
    elif rb or lb:  # 인접풍선이 하나이면
        ans += (rb + lb)
    else:  # 마지막 풍선인 경우
        ans += scores[num]
    return ans

def back_tracking(level, total, popped, N, path):
    global max_v, best
    if level == N:
        if max_v < total:
            max_v = total
            best = path.copy()
        return

    for i in range(1, N+1):  # 1번부터 선택
        if level == 0 and (i == 1 or i == N):  # 1번이나 N번부터 터뜨리는 경우는 제외
            continue
        if popped[i] == 0:  # 아직 안 터진 풍선이면
            popped[i] = 1  # i번 풍선을 쏘기
            back_tracking(level+1, total + cal_score(left(i, N), right(i, N), i), popped, N, path + [i])
            popped[i] = 0



T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 풍선의 개수 = 사격 횟수
    scores = [0]
    s = list(map(int, input().split()))
    scores.extend(s)
    popped = [0]*(N+1)
    max_v = 0
    best = []
    back_tracking(0, 0, popped, N, [])
    print(f'#{tc} {max_v}')
    print(best)


# def right(idx, N):  # 해당 인덱스를 기준으로 오른쪽 탐색
#     bn = idx+1
#     while bn <= N:
#         if popped[bn] == 0:
#             return scores[bn]
#         else:
#             bn += 1
#     return 0  # 오른쪽에 남은 풍선이 없다면
#
#
# def left(idx, N):
#     bn = idx-1
#     while bn >= 1:
#         if popped[bn] ==0:
#             return scores[bn]
#         else:
#             bn -= 1
#     return 0
#
#
# def cal_score(lb, rb, num):
#     ans = 0
#     if rb and lb:  # 인접풍선이 두 개이면
#         ans += (rb * lb)
#     elif rb or lb:  # 인접풍선이 하나이면
#         ans += (rb + lb)
#     else:  # 마지막 풍선인 경우
#         ans += scores[num]
#     return ans
#
# def back_tracking(level, popped, N, dp):
#     if level == N:
#         return 0
#
#     if dp[level] != -1:
#         return dp[level]
#
#     max_score = 0
#     for i in range(1, N+1):  # 1번부터 선택
#         if popped[i] == 0:  # 아직 안 터진 풍선이면
#             popped[i] = 1  # i번 풍선을 쏘기
#             max_score = max(max_score, cal_score(left(i, N), right(i, N), i), back_tracking(level+1, popped, N, dp))
#             popped[i] = 0
#     dp[level] = max_score
#     return max_score
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())  # 풍선의 개수 = 사격 횟수
#     scores = [0]
#     s = list(map(int, input().split()))
#     scores.extend(s)
#     popped = [0]*(N+1)
#     dp = [-1]*(N+1)
#     max_v = back_tracking(0, popped, N, dp)
#     print(f'#{tc} {max_v}')