# 피보나치 수열
# f(n) = f(n-1) + f(n-2), f(0) = 0, f(1) = 1
N = int(input())
# dp 초기화
dp = [-1] * 36
dp[1] = 0
dp[2] = 1

def fibo(n):
    if dp[n] != -1:  # n의 값이 이미 계산되어 있는 경우
        return dp[n]
    else: # 아직 계산 되지 않은 경우
        dp[n] = fibo(n - 1) + fibo(n - 2)  # 계산하고
        return dp[n]
print(fibo(N))

# 마실 수 있는 최대 와인의 양
#1<=n<=10,000
dp = [0]*10001  # 메모이제이션을 위한 배열 초기화
glass = [0]*10001

n = int(input())  # 포도주 잔의 개수
for i in range(1, n + 1):
    glass[i] = int(input())

dp[1] = glass[1]
dp[2] = glass[1]+glass[2]
for i in range(3, n+1):  # i번째 위치에서 가장 많이 마실 수 있는 포도주의 양
    dp[i] = max(dp[i-1], dp[i-2]+glass[i], dp[i-3]+glass[i-1]+glass[i])

print(dp[n]) #

# 최대 회의의 수
N = int(input())
lst = []
dp = [0] * N
for i in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
# 시작 시간이 이른 순으로 정렬
lst.sort(key=lambda x: x[0])
# dp배열 채우기
for i in range(N):
    s, e = lst[i]  # 기준점
    temp = []
    for j in range(0, i):  # 기준점보다 시작시간이 이른 경우만 고려
        if lst[j][1] <= s:  # 기준점의 시작시간보다 종료시간이 이르거나 같은 경우
            temp.append(dp[j])  # 해당 회의의 dp값을 저장
    if temp:  # 리스트가 비어있지 않다면
        dp[i] = max(temp) + 1
    else:  # 리스트가 비어있다면
        dp[i] = 0
print(max(dp)+1)