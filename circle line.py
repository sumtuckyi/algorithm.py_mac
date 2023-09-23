T = int(input())

def is_adjacent(x, y):
    if abs(x-y) != 1 and abs(x-y) != N-1:
        return 0
    return 1

for tc in range(1, T+1):
    N = int(input())  # 0부터 N-1번 정류장까지
    scores = list(map(int, input().split()))
    max_v = 0  # 타당도의 최댓값
    visited = [0]*(N+1)

    def back(level, path):
        global max_v
        tof = [1, 1, 1]
        if level == 4:
            total = 0
            for j in range(2):
                total += (scores[path[2*j]] + scores[path[2*j+1]])**2
            if total > max_v:
                print(path)
                max_v = total
            return
        # 1번을 뽑는 경우
        if level == 0:
            for i in range(N):
                if not visited[i]:  # 아직 추가되지 않은 정류장이라면
                    visited[i] = 1
                    back(level+1, path + [i])
                    visited[i] = 0
        elif level == 1:  # 2번을 뽑는 경우
            for i in range(N):
                if not visited[i]:
                    pre = path[-1]
                    if not is_adjacent(pre, i):  # 1번과 2번이 인접하지 않는다면
                        visited[i] = 1
                        back(level+1, path + [i])
                        visited[i] = 0
        elif level == 2:  # 3번을 뽑는 경우
            for i in range(N):
                if not visited[i]:
                    for j in range(2):
                        tof[j] = is_adjacent(path[j], i)
                    if not tof[0] and not tof[1]:  # 1-2번과 인접하지 않은 역인 경우
                        visited[i] = 1
                        back(level+1, path + [i])
                        visited[i] = 0
        elif level == 3:  # 4번을 뽑는 경우
            for i in range(N):
                if not visited[i]:
                    for j in range(3):
                        tof[j] = is_adjacent(path[j], i)
                    if not tof[0] and not tof[1] and not tof[2]:  # 1-3번과 인접하지 않은 역이고
                        # 교차여부 판단
                        o, p, q = path[0], path[1], path[2]
                        a, b = min(o, p), max(o, p)  # 노선 1
                        x, y = min(i, q), max(i, q)  # 노선 2
                        if (y < a) or (b < x) or (a < x and y < b) or (x < a and b < y):  # 두 노선이 교차하지 않는다면
                            visited[i] = 1
                            back(level+1, path + [i])
                            visited[i] = 0

    back(0,[])

    print(f'#{tc} {max_v}')







