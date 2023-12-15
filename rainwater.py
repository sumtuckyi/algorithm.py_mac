import sys

H, W = map(int, sys.stdin.readline().split()) #높이, 너비
blocks_heights = list(map(int, sys.stdin.readline().split()))
new_map = [[0 for _ in range(W)] for _ in range(H)]

# 블록이 쌓인 상황 구현하기
for i in range(W):
    h = blocks_heights[i]
    if h == 0:
        continue
    # 높이가 4인데 블록 높이가 3이면 0열의 1행부터 마지막 행까지 1로 바꿔주기
    # 블록 높이가 1이면 3행만 -> 즉, (H-블록높이)행부터 마지막 행까지 해당 열의 값을 바꿔주면 됨
    for row in range(H-h, H):
        new_map[row][i] = 1

# new_map을 돌면서 체크
volume = 0
for i in range(H):
    start_or_not = False  # 시작 블럭을 만났는지 여부
    not_closed = True  # 닫힘 블럭을 만났는지 여부
    cnt = 0 # 행별로 계산
    for j in range(W):
        # if j == W-1: # 마지막 칸에 도달
        #     end_reached = True
        if new_map[i][j]: # 1인데
            if not start_or_not: #시작블럭이면
                start_or_not = True
            elif start_or_not and not_closed: # 시작블럭이 있었고 안 닫혔다면
                volume += cnt # 지금까지 만난 빗물을 저장하고
                # print('더해지는 값:', cnt)
                cnt = 0 # 초기화
                # print('더해지는 시점의 좌표:', i, j)

        elif not new_map[i][j]: # 0이면
            if start_or_not and not_closed: # 시작블럭이 있고 아직 안 닫힌 경우
                cnt += 1

print(volume)
