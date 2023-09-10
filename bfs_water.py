from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 지도의 행과 열
    b = [list(input()) for _ in range(N)]
    w = []
    q = deque()
    total = 0
    cnt = [[-1 for _ in range(M)] for _ in range(N)]
    # 물인 지점을 저장
    for i in range(N):
        for j in range(M):
            if b[i][j] == 'W':
                q.append((i, j))
                cnt[i][j] = 0
    # 물인 칸을 기준으로 탐색
    # 물인 칸을 모두 큐에 넣기
    while q:
        x, y = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+di < N and 0 <= y+dj < M:
                if cnt[x+di][y+dj] == -1:  # 아직 방문하지 않은 땅이라면
                    cnt[x+di][y+dj] = cnt[x][y] + 1  # 물로부터의 거리 구해주기
                    q.append((x+di, y+dj))  # 새로운 기준점으로
    for i in range(N):
        for j in range(M):
            total += cnt[i][j]
    print(f'#{tc} {total}')
