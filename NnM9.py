N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0]*N
nums.sort()
# set로 중복체크 - list를 tuple로 변환해야함
# 아니면 그냥 list와 in 연산자를 사용해서 확인
dup_check = set() # dup_check = []


def backtracking(depth, path):
    if depth == M:
        print(path)
        t = tuple(path)
        # 수열의 중복 여부 체크
        if t in dup_check:
            return
        else:
            dup_check.add(t)
            print(*path)
            return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        backtracking(depth + 1, path + [nums[i]])
        visited[i] = 0

# backtracking(0, [])

# check의 중복여부를 확인할 list
check_lists = []
check = [0]*10001
def backtracking2(depth, path, check):
    if depth == M:
        if check in check_lists:
            return
        else:
            check_lists.append(check.copy())
            print(*path)
            return

    for i in range(N):
        if visited[i]:
            continue
        if len(path) and nums[i] < path[-1]:
            continue
        visited[i] = 1
        check[nums[i]] += 1
        backtracking2(depth + 1, path + [nums[i]], check)
        visited[i] = 0
        check[nums[i]] -= 1


# backtracking2(0, [], check)

nums2 = list(set(nums))
nums2.sort()

def backtracking3(depth, path):
    if depth == M:
        print(*path)
        return

    for i in range(len(nums2)):
        if len(path) and nums2[i] < path[-1]:
            continue
        backtracking3(depth + 1, path + [nums2[i]])


backtracking3(0, [])