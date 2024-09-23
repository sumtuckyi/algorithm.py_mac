N = int(input())

nums = []
rank = [0 for _ in range(N)]
for i in range(N):
    p = list(map(int, input().split()))
    nums.append(p+[i])

nums.sort(key = lambda x:x[0], reverse=True)

for i in range(N):
    for j in range(i): # i번째 사람보다 몸무게가 많이 나가는 사람이랑만 키를 비교
        if nums[j][0] <= nums[i][0]:
            continue
        if nums[j][1] <= nums[i][1]:
            continue
        rank[nums[i][2]] += 1 # i번째 사람보다 덩치가 큰 사람


print(*[x + 1 for x in rank])