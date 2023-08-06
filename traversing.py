# 지그재그 순회
m, n = 4, 3
arr = [[1] * m for _ in range(n)]
print(arr)
for i in range(n):  # n은 행의 수
    for j in range(m):  # m은 열의 수
        arr[i][j + (m-1-2*j) * (i%2)] = i  # 홀수번째 행일 때에만 j의 값이 증가할수록 열의 인덱스는 감소한다.(즉, 오른쪽에서 왼쪽으로 탐색)

# 4방향 순회
import random

a_list = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]


def cal_abs(new_list):

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    max_v = 0
    result = 0
    for i in range(5):
        for j in range(5):
            direction = 0
            total = 0
            while direction < 4:  # 4방향에 대해 각 한 번 씩만 탐색할 것
                y, x = j, i  # 기준점
                current = new_list[j][i]  # 기준점의 값
                y, x = y+dy[direction], x+dx[direction]
                if 0 <= y <= 4 and 0 <= x <= 4 :  # 유효한 인덱스인지 검사
                    total += abs(current - new_list[y][x])
                    direction += 1
                else:
                    direction += 1
            result += total
            if max_v < total:
                max_v = total
    return result


a = cal_abs(a_list)
print(a)