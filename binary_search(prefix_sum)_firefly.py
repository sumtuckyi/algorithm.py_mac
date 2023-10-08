# 누적합으로 풀기
import sys

N, H = map(int, sys.stdin.readline().split())
top = [0 for _ in range(H+1)]
bottom = [0 for _ in range(H+1)]
ans = float('inf')  # 장애물의 최솟값
cnt = 0  # 구간의 개수
for i in range(N):
    height = int(sys.stdin.readline())
    if i % 2 == 0:  # 짝수 번째 장애물
        bottom[height] += 1
    else:
        top[H-height+1] += 1

# 누적합 구하기
for j in range(2, H+1):
    top[j] += top[j-1]
for k in range(H-2, 0, -1):
    bottom[k] += bottom[k+1]

# 최솟값 찾기(구간은 1부터 H까지)
for l in range(1, H+1):
    temp = top[l] + bottom[l]
    if ans > temp:
        ans = temp  # 최솟값 갱신
        cnt = 1
    elif ans == temp: # 중복값 발생 시, 카운트만
        cnt += 1

print(ans, cnt)



