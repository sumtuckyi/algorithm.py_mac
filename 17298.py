# 수열의 길이가 최대 100만이므로 한 번의 탐색으로 작업 수행할 것
N = int(input())
nums = list(map(int, input().split()))
res = [-1] * N
stack = []
# 뒤에서부터 탐색?
# 스택의 아래에 있을수록 더 멀리 있는 수이다.
for i in range(N - 1, -1, -1):
    while stack and stack[-1] <= nums[i]: # 스택에 수가 있고, 가장 상위 요소가 현재 수보다 작거나 같은한
        stack.pop() # 스택 상위 요소 제거

    if stack: # 제거 후에도 아직 수가 남아있다면 - 그 수는 nums[i]보다 큰 가장 가까운 수이다.
        res[i] = stack[-1]

    stack.append(nums[i])

print(*res)
