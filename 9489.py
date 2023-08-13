T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로 길이
    data = [list(map(int, input().split())) for _ in range(N)]


    # 두칸씩 비교
    def max_length(arr):
        max_l = 1  # 구조물은 길이가 최소 2
        # 행탐색
        for i in range(0, N):
            cnt = 1
            for j in range(1, M):
                if arr[i][j-1] == arr[i][j] == 1:
                    cnt += 1
                    if j == M-1 and max_l < cnt:  # 행의 마지막 요소까지 탐색을 마친 경우
                        max_l = cnt
                else:  # 0-1이거나 1-0인 경우나 0-0인 경우
                    if max_l < cnt:
                        max_l = cnt
                    cnt = 1

        # 열탐색
        for i in range(0, M):
            for k in range(1, N):
                if arr[k-1][i] == arr[k][i] == 1:
                    cnt += 1
                    if i == N-1 and max_l < cnt:
                        max_l = cnt
                else:
                    if max_l < cnt:
                        max_l = cnt
                    cnt = 1

        return max_l

    # 한칸씩 비교
    # def max_length(arr):
    #     max_l = 1  # 구조물은 길이가 최소 2
    #     # 행탐색
    #     for i in range(0, N):
    #         cnt = 0
    #         for j in range(0, M):
    #             if arr[i][j] == 1:
    #                 cnt += 1
    #                 if j == M-1 and max_l < cnt:  # 행의 마지막 요소까지 탐색을 마친 경우
    #                     max_l = cnt
    #             else:  # 0-1이거나 1-0인 경우나 0-0인 경우
    #                 if max_l < cnt:
    #                     max_l = cnt
    #                 cnt = 0
    #
    #     # 열탐색
    #     for i in range(0, M):
    #         cnt = 0
    #         for k in range(0, N):
    #             if arr[k][i] == 1:
    #                 cnt += 1
    #                 if k == N-1 and max_l < cnt:
    #                     max_l = cnt
    #             else:
    #                 if max_l < cnt:
    #                     max_l = cnt
    #                 cnt = 0
    #
    #     return max_l

    print(f'#{tc} {max_length(data)}')


