N, M = map(int, input().split()) # 구슬의 개수, 그룹의 수

marbles = list(map(int, input().split())) # 각 구슬에 적힌 번호

# N개의 수를 M개의 그룹으로 나눴을 때 최댓값의 최솟값
dp = [[987654321 for _ in range(M + 1)] for _ in range(N)]
# N개의 수를 M개의 그룹으로 나눴을 때 가장 우측 그룹의 구슬의 수
cnt = [[987654321 for _ in range(M + 1)] for _ in range(N)]

sum = 0
# i개의 구슬로 1개의 그룹을 만들 때 최솟값의 최댓값 => i개 구슬의 합
for i in range(0, N):
    sum += marbles[i]
    dp[i][1] = sum
    cnt[i][1] = i + 1

for i in range(N):
    for j in range(1, M + 1):
        print(i, j)
        total = 0
        for k in range(i, 1 - 1, -1): # k가 i인 경우부터 1까지 역으로 순회
            total += marbles[k] # k번째 구슬을 추가하려는 경우
            # 그룹 중 최댓값 찾기
            min_sum = max(dp[k - 1][j - 1], total) # 제일 우측의 그룹 sum과 그 그룹을 빼고 j-1개의 그룹을 만들 때의 최댓값의 최솟값을 비교
            print('min_sum 갱신됨: ', min_sum)
            print('total: ', total)
            if dp[i][j] > min_sum: # 최댓값 중 최솟값 찾기
                cnt[i][j] = i - k + 1
                dp[i][j] = min_sum

print(dp, cnt)
ans = dp[N - 1][M] # N개의 구슬을 M개의 그룹으로 나눴을 때 최댓값의 최솟값

arr = []
temp = N - 1 # 전체 구슬 개수
for i in range(M, 1 - 1, -1): # M부터 1까지(그룹의 수) 각 그룹에 속한 구슬의 수
    arr.append(cnt[temp][i]) # 가장 우측 그룹의 구슬 개수
    temp -= cnt[temp][i]

arr.reverse()

print(ans)
print(*arr)



