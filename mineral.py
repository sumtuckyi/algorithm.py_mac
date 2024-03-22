from collections import deque
R, C = map(int, input().split()) # 행, 열의 수

cave = [list(input()) for _ in range(R)] # 동굴의 상태
N = int(input()) # 막대를 던진 횟수
total_mineral = 0 # 최초 미네랄의 개수

heights = list(map(int, input().split())) # 막대를 던지는 높이
clusters = []

for i in range(R):
    for j in range(C):
        if cave[i][j] == 'x':
            total_mineral += 1 # 최초 미네랄의 개수 카운트
print(total_mineral)
# 미네랄 제거 함수 - row높이에서 막대를 던진 경우
def crash(row, LoR):
    # 왼쪽에서 던진 경우
    if LoR == 'L':
        for i in range(C):
            if cave[R-row][i] == 'x':
                cave[R-row][i] = '.'
                break
    # 오른쪽에서 던진 경우
    else:
        for i in range(C-1, -1, -1):
            if cave[R-row][i] == 'x':
                cave[R-row][i] = '.'
                break
    # print('막대에 부딪힌 결과', cave)
    return

# 클러스터의 개수 확인 함수 - bfs
def bfs(start_x, start_y, visited):
    q = deque()
    q.append((start_x, start_y))
    temp = [(start_x, start_y)]
    cnt = 1  # 너비우선탐색 시작점 포함
    while q:
        cx, cy = q.popleft()
        visited[cx][cy] = 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= cx + dx < R and 0 <= cy + dy < C:
                if visited[cx + dx][cy + dy] == 1:
                    continue
                if cave[cx + dx][cy + dy] == 'x':
                    q.append((cx + dx, cy + dy))
                    temp.append((cx + dx, cy + dy))
                    # print(f'({cx + dx}, {cy + dy})가 미네랄이 있는 칸이니 카운트')
                    cnt += 1
                    visited[cx + dx][cy + dy] = 1
    clusters.append(temp)
    return cnt # 하나의 클러스터에 포함된 미네랄의 개수 리턴

# 각 턴에서 한 번만 호출
def count_cluster(): # remain은 최초 미네랄의 개수 - 막대를 던진 횟수
    global clusters
    clusters = []
    visited = [[0 for _ in range(C)] for _ in range(R)] # bfs 실행시 방문여부 표시
    tof = False
    cnt = 0
    # 큐에 너비 우선 탐색 시작점 저장
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x':
                if visited[i][j] == 1:
                    continue
                print('막대에 부딪힌 미네랄을 없애고 count_cluster 여기서 탐색 시작', (i, j))
                for row in cave:
                    print(''.join(row))
                cnt += bfs(i, j, visited) # 해당 좌표를 기준으로 너비우선탐색
                print('현재까지의 cnt ', cnt)
            #     if cnt == remain: # 클러스터가 하나
            #         print('bfs결과, 남은 미네랄 수와 카운트 한 미네랄 수가 일치함')
            #         tof = True
            #         break
            # if tof:
            #     break # 반복문 탈출
    # clusters에 모든 클러스터가 각각 하나의 배열로 저장됨

# 클러스터 이동 함수
def gravity():
    # 각 클러스터를 가장 아래 행부터 돌면서 아래로 수직낙하하는 상황인지 판별하기
    # print('gravity가 호출됨', clusters)
    for i in range(len(clusters)): # 하나의 클러스터에 대해 수행
        # 가장 아래행부터 돌도록 정렬
        sorted_cluster = sorted(clusters[i], key=lambda x: x[0], reverse=True)
        # 해당 클러스터가 이미 바닥에 있는 경우 - 패스(더이상 떨어질 수 없음)
        if sorted_cluster[0][0] == R - 1:
            # print('이 클러스터는 이미 바닥에 있으므로 패스', sorted_cluster)
            continue
        # 그게 아니라면 아래가 비어있는지 더이상 떨어질 수 없을 때까지 확인
        while True:
            print('이 클러스터는 바닥에 있지 않음', sorted_cluster)
            for i in range(len(sorted_cluster)): # 하나의 클러스터를 한 칸씩 돌기
                x, y = sorted_cluster[i][0], sorted_cluster[i][1]
                if (x+1) <= R-1 and ((x+1, y) in sorted_cluster or cave[x + 1][y] == '.'):
                # if (x+1) <= R-1 and cave[x + 1][y] == '.' : # 이동할 칸이 범위 내에 있고 빈칸이면
                    continue  # 다음 칸을 체크
                else:
                    # 더 이상 이동이 불가한 경우 리턴
                    print(f'({x},{y})에서 더 이상 이동 불가..')
                    for row in cave:
                        print(''.join(row))
                    return
            # 반복문을 무사히 돌았다면
            # 전체 클러스터를 한 칸씩 이동시키기
            for i in range(len(sorted_cluster)): # 하나의 클러스터를 한 칸씩 돌기
                x, y = sorted_cluster[i][0], sorted_cluster[i][1]
                cave[x + 1][y] = 'x'
                cave[x][y] = '.'
                sorted_cluster[i] = (x + 1, y)
                print(f'중력에 의해 ({x}, {y})에서 ({x + 1}, {y})로 이동 중...')
            print('전체 클러스터 이동 완료!')
            for row in cave:
                print(''.join(row))


for i in range(1, N + 1):
    if i % 2: # 홀수번째 순서 - 왼쪽
        crash(heights[i-1], 'L')
    else:
        crash(heights[i-1], 'R')
    count_cluster()  # 클러스터 조사완료
    print('count_cluster 종료', clusters)
    # 이동할 클러스터가 있는지 확인(클러스터가 1개라도 이동 가능)
    gravity()
    print('gravity에서 return')

for row in cave:
    print(''.join(row))