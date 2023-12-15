T = int(input())

def recur(cur, weight): # cur번 물건을 담을지 선택하는 경우, 이미 weight만큼 담은 상황에서 얻을 수 있는 최대 가치
    # print('cur', cur, 'w', weight)
    # 기저조건
    if weight > K:
        return -1000
    if cur == N + 1:
        return 0
    # 이미 계산한 적이 있다면
    if dp[cur][weight] != -1:
        # print(dp[cur][weight])
        return dp[cur][weight]
    # 처음 계산하는 거라면
    dp[cur][weight] = max(recur(cur + 1, weight + arr[cur][0]) + arr[cur][1], recur(cur + 1, weight))
    return dp[cur][weight]


for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 물건의 개수와 가방의 부피
    arr = [[] for _ in range(N + 1)]
    dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
    answer = 0
    for i in range(1, N + 1):
        v, c = map(int, input().split())
        arr[i].extend((v, c))
    print(recur(1, 0))
