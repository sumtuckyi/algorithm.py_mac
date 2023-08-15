#재귀함수를 이용해 모든 경우의 수 구하기
def recursive(y, x, shape):  # 파이프의 오른쪽 끝 위치와 현재 파이프의 상태를 전달하고 파이프를 이동시킬 위치를 검사하는 함수
    global ans
    # 5개의 조건문이 참인지 순차적으로 검토(파이프를 이동시킬 위치를 검토)
    # 종료 조건
    if y > n or x > n:  # 파이프의 위치가 집의 범위를 넘어선 경우
        return
    if y == n and x == n:  # 파이프가 목적지에 도착한 경우(이 경우 경우의 수를 카운트하고 다음 조건문으로 넘어가 조건문이 참이 되더라도 어차피 재귀 호출의 결과 파이프의 위치가 집의 범위를 넘어서게 되므로 함수가 종료됨))
        ans += 1
    if home[y][x+1] == 0 and (shape == 0 or shape ==2):  # 기준점의 오른쪽이 벽이 아니고 현재 상태가 가로거나 대각선인 경우 재귀함수 호출(가로로 이동)
        recursive(y, x+1, 0)
    if home[y+1][x] == 0 and (shape == 1 or shape == 2):  # 기준점의 아래쪽이 벽이 아니고 현재 상태가 세로거나 대각선인 경우(세로로 이동)
        recursive(y+1, x, 1)
    if home[y+1][x] == 0 and home[y][x+1] == 0 and home[x+1][y+1] ==0:  # 기준점의 오른쪽, 아래쪽 대각선 아래가 모두 벽이 아닌 경우(대각선으로 이동)
        recursive(y+1, x+1, 2)

n = int(input())
home = [[0 for _ in range(18)] for _ in range(18)]  # 18x18배열
# 3 <= n <= 16이므로 최댓값일 경우보다 2칸 여유있게 배열을 만든다.
for i in range(1, n+1):
    row = list(map(int, input().split())) # 집의 구조를 한 줄씩 입력받아서
    for j in range(1, n+1): # home을 1부터 n행과 n열까지만 채우기
        home[i][j] = row[j-1]

ans = 0  # 구하고자 하는 경우의 수
recursive(1, 2, 0)  # 파이프의 초기 위치와 상태는 고정조건
print(ans)
