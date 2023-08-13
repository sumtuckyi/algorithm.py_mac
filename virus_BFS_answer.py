from collections import deque

visit = [[0 for col in range(10)] for row in range(10)]  # bfs함수에서 바이러스 이동 칸을 표시하기 위한 배열
visit2 = [[0 for col in range(10)] for row in range(10)]  # 백트래킹 함수에서 선택한 빈칸을 표시하기 위한 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():  # 3칸을 모두 선택하면 함수가 호출됨
    global answer
    # 연구소를 탐색
    for x in range(n):
        for y in range(m):
            visit[x][y] = lab[x][y]  # visit배열에 연구소의 상태를 그대로 옮김
            if lab[x][y] == 2:  # 그 과정에서 2인 칸을 만나면 큐에 그 좌표를 저장
                queue.append([x, y])

    while queue:
        x, y = queue.popleft()  # 큐의 전단의 데이터를 꺼내서 현재 위치로 설정
        visit[x][y] = 1  # 큐에서 꺼낸 좌표는 바이러스의 위치이므로 다시 탐색하지 않도록 그 값을 1로 바꿈
        for i in range(4):  # 바이러스의 위치를 중심으로 상하좌우로 탐색
            # 이동할 칸이 맵의 범위 내에 있고, 연구소 배열에서 그 값이 0(벽이 없는 곳)이고, visit 배열에서 그 값이 0(아직 방문하지 않은 칸)이면
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and lab[x+dx[i]][y+dy[i]]==0 and visit[x+dx[i]][y+dy[i]]==0:
                queue.append([x+dx[i], y+dy[i]])  # 큐에 해당 칸의 좌표를 삽입
                visit[x+dx[i]][y+dy[i]] = 1  # 해당 칸을 방문했음을 표시

    cnt = 0
    for x in range(n):
        for y in range(m):
            # 연구실에서 해당 좌표가 0이고(즉, 벽이 세워지지 않았음), visit배열의 해당 좌표가 0인 경우(즉, 바이러스가 퍼지지 않았음)
            if lab[x][y] == 0 and visit[x][y] == 0:
                cnt += 1
    answer = max(answer, cnt)

def back_tracking(select):

    if select == 3:  # 벽을 세울 빈칸을 3곳 선택한 경우에 bfs함수를 실행한 후 return
        bfs()  # 함수가 호출되면 2인 칸을 중심으로 상하좌우로 바이러스를 퍼뜨린 결과 0인 칸의 개수를 세어 최댓값(answer)이 되는 경우를 갱신함
        return
    for x in range(n):
        for y in range(m):
            if not lab[x][y] and not visit2[x][y]:  # 연구소에서 해당 칸이 0이고 해당 칸을 선택한 적이 없다면(각기 다른 곳에 3개를 세워야하기 때문에)
                visit2[x][y] = 1  # 해당칸을 선택했음을 표시하고
                lab[x][y] = 1  # 연구실에 벽을 세움
                back_tracking(select+1) # 한 개를 선택하였으므로 select에 1을 더하여 재귀 호출
                lab[x][y]=0  # 백트래킹 함수가 종료된 후 다시 중단지점으로 돌아와서
                visit2[x][y]=0  # 선택했던 빈칸을 해제한다.

queue = deque()
answer = 0  # 최댓값을 저장할 변수
n, m = map(int, input().split())  # 연구소의 세로, 가로 크기
lab = [list(map(int, input().split())) for _ in range(n)]  # 연구소의 상태를 입력받아 저장
back_tracking(0)  # 빈칸을 선택한 횟수
print(answer)

'''
백트래킹 함수를 재귀호출 한다 -> 현시점에서 가장 깊은 정점으로 끝까지 가서 더 이상 인접 노드가 없으면(재귀 함수가 종료되어야 할 깊이에 도달하면)
가장 가까운 갈림길 노드로 가서 탐색하지 않은 하위 노드를 다시 탐색(재귀호출)
'''