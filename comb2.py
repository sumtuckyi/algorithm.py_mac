d_odd = [(-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
d_even = [(-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1)]


def back_tracking(path, level):  # (x,y)를 첫번째 셀로 패스에 추가했을 때 가능한 모든 경우에서의 사용자 수를 계산
    if level == 3:
        total = 0
        path.sort() # 디버깅용
        for a, b in path:
            total += comb[a][b]
        result.append(total)
        # if path == [(1, 2), (1, 3), (1, 4), (2, 3)] or path == [(0,0), (0,1), (1, 1), (2, 2)] or path == [(1,3), (1, 4), (2, 3), (2, 4)] or path == [(0,1),(1,1), (1, 2), (1,3)] or path == [(0,2), (0, 3), (1,1), (1, 2)]:
        #     print(path, total)
        return

    for i, j in path:
        if j % 2 == 0: #짝수 열의 경우
            for di, dj in d_even: # 해당 지점의 인접 셀에 대해
                if 0 <= i + di < H and 0 <= j + dj < W: # 범위 안에 있고
                    if visited[i + di][j + dj] == 0:  # 아직 추가되지 않았다면
                        visited[i + di][j + dj] = 1
                        back_tracking(path + [(i+di, j+dj)], level + 1)
                        visited[i+di][j+dj] = 0
        else:  #홀수 열인 경우
            for di, dj in d_odd: # 해당 지점의 인접 셀에 대해
                if 0 <= i + di < H and 0 <= j + dj < W: # 범위 안에 있고
                    if visited[i + di][j + dj] == 0:  # 아직 추가되지 않았다면
                        visited[i + di][j + dj] = 1
                        back_tracking(path + [(i+di, j+dj)], level + 1)
                        visited[i+di][j+dj] = 0


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    comb = [list(map(int, input().split())) for _ in range(H)]  # 셀별 사용자 수
    result = []  # 4개의 셀을 선택하는 모든 경우에서 각각의 편익
    for i in range(H):
        for j in range(W):
            # 한 개의 셀을 시작점으로 선택할 때마다 방문확인 배열 초기화
            visited = [[0 for _ in range(W)] for _ in range(H)]
            visited[i][j] = 1  # 패스에 추가된 셀을 체크
            back_tracking([(i, j)], 0)

    print(f'#{tc} {max(result)}')