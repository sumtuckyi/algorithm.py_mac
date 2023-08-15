import sys
n = int(sys.stdin.readline())  # 전체 종이의 한 변의 길이

colorPaper = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]  # 전체 색종이의 상태

white = 0
blue = 0

def divide_and_conquer(x, y, n):  # 현재 좌표와 탐색할 해당 구역의 크기를 인자로 받는다.
    global blue, white
    same_color = colorPaper[x][y]  # 해당 구역이 모두 같은 색인지 확인하기 위한 기준 변수
    for i in range(x, x+n):
        for j in range(y, y+n):
            if same_color != colorPaper[i][j]:  # 해당 구역의 기준색과 다른색이 있다면
                # 해당 구역을 4등분 하여 분할정복을 시작한다.
                divide_and_conquer(x, y, n//2)
                divide_and_conquer(x, y+n//2, n//2)
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)
                return
    # 함수가 호출되고 해당 구역에서 기준색과 다른색이 없었다면 이하 코드가 실행된다.
    if same_color == 0:  # 해당 구역의 기준색이 하얀색이면
        white += 1
        return
    else:  # 해당 구역의 기준색이 파란색이면
        blue += 1
        return

divide_and_conquer(0, 0, n)
print(white)
print(blue)
