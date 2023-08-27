T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 업무의 수
    data = []  # 노드와 간선 정보 저장
    for i in range(N):
        data.append(list(map(int, input().split())))
    dp = [0]*(N+1)
    for i in range(1, N+1):
        if len(data[i-1]) == 2:  # 사전 업무가 없다면
            dp[i] = data[i-1][0]  # 자신의 업무만 고려
        for num in data[i-1][2:]:
            dp[i] = max(dp[i], dp[num]+data[i-1][0])
    print(dp)