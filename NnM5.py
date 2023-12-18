N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0]*(N)
nums.sort()


def backtracking(depth, path):
    if depth == M:
        print(*path)
        return

    for i in range(N):
        # if visited[i]:
        #     continue
        # # 수열의 중복을 제거하고 싶다면 해당 조건 추가
        if len(path) and nums[i] < path[-1]:
            continue
        # visited[i] = 1
        backtracking(depth + 1, path + [nums[i]])
        # visited[i] = 0


backtracking(0, [])