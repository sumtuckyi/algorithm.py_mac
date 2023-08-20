# from collections import defaultdict
# T = int(input())
#
#
# def scoring(student):
#     score = 0
#     point = 1  # 문제의 배점
#     pre = False
#
#     for i in range(M):  # 각 문제에 대하여
#         if sheets[student][i] == ans[i]:  # 답안지의 답과 같으면
#             if pre:  # 바로 전 문제가 정답이었으면
#                 point += 1
#                 score += point
#             else:
#                 score += point
#                 pre = True
#         else:  # 오답이면
#             point = 1  # 배점 초기화
#             pre = False
#     return score
#
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     ans = list(map(int, input().split()))  # 답안지 리스트
#     sheets = defaultdict(list)
#     scores = []
#     for i in range(1, N + 1):  # N개의 답안지를 딕셔너리에 저장
#         ans_sheet = list(map(int, input().split()))  # 각 학생의 답안지
#         sheets[i].extend(ans_sheet)
#     for j in range(1, N + 1):
#         scores.append(scoring(j))
#     print(f'#{tc} {max(scores)-min(scores)}')


T = int(input())


def scoring(sheet): # 학생 번호와 답안지를 인자로 받음
    score = 0
    point = 1  # 문제의 배점
    pre = False
    for i in range(M):  # 각 문제에 대하여
        if sheet[i] == ans[i]:  # 답안지의 답과 같으면
            if pre:  # 바로 전 문제가 정답이었으면
                point += 1
                score += point
            else:
                score += point
                pre = True
        else:  # 오답이면
            point = 1  # 배점 초기화
            pre = False
    return score


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))  # 답안지 리스트
    scores = []
    for i in range(1, N + 1):  # N개의 답안지를 딕셔너리에 저장
        ans_sheet = list(map(int, input().split()))  # 각 학생의 답안지
        scores.append(scoring(ans_sheet))

    print(f'#{tc} {max(scores)-min(scores)}')
