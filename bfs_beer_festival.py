from collections import deque
T = int(input())


def bfs():
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(1, N + 2):
            if visited[i] == 1:
                continue
            if (abs(cur_x - coordinates[i][0]) + abs(cur_y - coordinates[i][1])) <= 1000:
                q.append((coordinates[i][0], coordinates[i][1]))
                visited[i] = 1
    if visited[N + 1]:
        return "happy"
    else:
        return "sad"


for _ in range(T):

    coordinates = []
    N = int(input()) # 편의점의 개수
    start_x, start_y = map(int, input().split()) # 집 좌표
    q = deque([(start_x, start_y)])
    coordinates.append((start_x, start_y))
    for i in range(N): # 편의점의 좌표 입력받기
        x, y = map(int, input().split())
        coordinates.append((x, y))
    fest_x, fest_y = map(int, input().split()) # 페스티벌 장소 좌표
    coordinates.append((fest_x, fest_y))
    visited = [0 for _ in range(N + 2)]
    visited[0] = 1 # 시작점 방문 확인
    res = bfs()
    print(res)


