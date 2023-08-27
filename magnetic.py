T = 10
for tc in range(1, T + 1):
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    cnt = 0

    for i in range(N):  # 각 열에 대해
        s = []
        for j in range(N):
            if not s and table[j][i] == '1':  # 스택이 비어있고 N극인 경우
                s.append('1')
            elif s:  # 스택이 비어있지 않은 경우
                if s[-1] == '1' and (table[j][i] == '2'):  # N극 다음에 S극이 오는 경우
                    cnt += 1  # 카운트
                    s.append('2')
                elif s[-1] == '2' and (table[j][i] == '1'):  # S극 다음에 N극이 오는 경우
                    s.append('1') # 쌓기만 하고 카운트는 안 함
    print(f'#{tc} {cnt}')
