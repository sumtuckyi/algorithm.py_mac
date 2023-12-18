N, M = map(int, input().split())
visited = [0]*(N+1)
# def backtracking(depth, path):
#     # 종료조건
#     if depth == M:
#         print(*path)
#         return
#
#     # 1부터 N까지의 자연수 중에서 중복없이 선택
#     for i in range(1, N + 1):
#         if visited[i] == 0:
#             visited[i] = 1
#             backtracking(depth + 1, path + [i])
#             visited[i] = 0


def backtracking2(depth, path):
    if depth == M:
        print(*path)
        return

    for i in range(1, N + 1):
        if visited[i] == 0:
            if len(path) and i < path[-1]:
                continue
            visited[i] = 1
            backtracking2(depth + 1, path + [i])
            visited[i] = 0


def backtracking3(depth, path):
    if depth == M:
        print(*path)
        return

    for i in range(1, N + 1):
        backtracking3(depth + 1, path + [i])


def backtracking4(depth, path):
    if depth == M:
        print(*path)
        return

    for i in range(1, N + 1):
        if len(path) and i < path[-1]:
            continue
        backtracking4(depth + 1, path + [i])


# backtracking(0, [])
# backtracking2(0, [])
# backtracking3(0, [])
backtracking4(0, [])