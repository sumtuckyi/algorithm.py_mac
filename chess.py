N, M = map(int, input().split())  # 행과 열의 수
b =[list(input()) for _ in range(N)]

min_v = 65
# 보드를 가능한 모든 경우별로 자르기
for i in range(0, N-7):
    for j in range(0, M-7):
        top_left = (i, j)
        pw = pb = 0  # 다시 칠해야 하는 칸의 수
        # 8x8단위로 확인
        for x in range(i, i+8):
            for y in range(j, j+8):
                if not ((x+y)%2) and b[x][y] != 'B':  # 짝수행 짝수열인데 W가 아닌 경우
                    pw += 1
                if (x+y)%2 and b[x][y] != 'W':
                    pw += 1
                if not ((x+y)%2) and b[x][y] != 'W':  # 짝수행 짝수열인데 W가 아닌 경우
                    pb += 1
                if (x+y)%2 and b[x][y] != 'B':
                    pb += 1
        min_v = min(min_v, pw, pb)
print(min_v)