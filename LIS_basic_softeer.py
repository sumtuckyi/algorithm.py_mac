import sys

N = int(input())
arr = list(map(int, input().split()))
# i에서 끝나는 최장 증가 부분수열의 길이
dp = [1]*N

for i in range(1, N):
    for j in range(i): # i번째 수에 대해서 i-1까지의 수와 각각 비교
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))