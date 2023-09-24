# 제출본
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 업무의 수
    data = []  # 노드와 간선 정보 저장
    t = [0]
    for i in range(N):
        task = list(map(int, input().split()))
        data.append(task)
        t.append(task[0])
    d = [0]*(N+1)  # 진입차수 초기화, 0번째 비움
    adj_lst = [[] for _ in range(N+1)]  # 인접리스트(진출차수 저장), 0번째 비움
    result = 0
    for i in range(N):
        if data[i][1] != 0:  # 진입차수가 0이 아닌 노드인 경우
            d[i+1] = data[i][1]  # 진입차수 저장
            for j in range(2, 2+data[i][1]):
                adj_lst[data[i][j]].append(i+1)
    coco = []
    # 모든 경우의 수 탐색
    for k in range(N):
        origin = t[k+1]
        t[k+1] = t[k+1] // 2  # k번째 작업을 코코가 도와주는 경우
        dp = [0] * (N + 1)
        temp = d.copy()
        q = deque()
        for i in range(1, N+1):
            if not temp[i]:
                q.append(i)
                dp[i] = t[i]
        while q:
            cur = q.popleft()
            if adj_lst[cur]:
                # adj_lst[cur].sort()
                for e in list(adj_lst[cur]):
                    temp[e] -= 1
                    dp[e] = max(dp[cur] + t[e], dp[e])
                    if temp[e] == 0:
                        q.append(e)
        # 큐가 비었는데 아직 처리되지 않은 일들이 남은 경우 -> 사이클 존재
        if len(set(temp)) != 1:
            result = -1
            break
        coco.append(max(dp))
        t[k+1] = origin

    ans = result if result == -1 else min(coco)
    print(f'#{tc} {ans}')