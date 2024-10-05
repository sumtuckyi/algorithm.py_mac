T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 물건의 개수와 가방의 부피
    cost = [0]
    weight = [0]
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        v, c = map(int, input().split())
        weight.append(v)
        cost.append(c)
    # dp배열 채우기
    for i in range(1, N + 1): # i번째 물건을 담을 지 말 지 결정할 차레
        for j in range(K + 1): # 배낭의 남은 용량(0부터 최대용량인 K까지)
            dp[i][j] = dp[i - 1][j] # 현재 물건을 담지 않은 경우를 기본값으로 설정
            if weight[i] <= j: # 현재 고려하는 물건의 무게가 남은 용량과 같거나 작은 경우만 고려
                dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i]] + cost[i])

    print(f'#{tc} {dp[N][K]}')