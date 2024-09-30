from collections import defaultdict
N = int(input())
nums = list(map(int, input().split()))
nums.sort()  # 오름차순 정렬

s = set()
a = set()

dict = defaultdict(int)
for i in range(N):
    dict[nums[i]] += 1

for i in range(N - 1):
    if nums[i] in a:
        continue
    a.add(nums[i])
    for j in range(i + 1, N):
        total = nums[i] + nums[j]
        if nums[i] == 0 and nums[j] != 0:
            if dict[nums[j]] < 2:
                continue
        if nums[i] != 0 and nums[j] == 0:
            if dict[nums[i]] < 2:
                continue
        if nums[i] == nums[j] == 0:
            if dict[0] < 3:
                continue
        s.add(total)
ans = 0
for num in nums:
    if num in s:
        ans += 1

print(ans)