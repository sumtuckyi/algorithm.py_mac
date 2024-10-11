# 그리디라기 보다는 구현 같음
N = int(input())  # 1부터 10까지

p = [0] + list(map(int, input().split()))


ans = [0]*N
for i in range(1, N + 1): # 1번부터 N번까지 자리를 찾아주기
    if i == 1:
        ans[p[i]] = i
    else: # i가 3이상인 경우
        seats = p[i] # ans를 앞에서부터 탐색할 때, 빈 자리가 seats만큼 남아있어야 한다.
        cnt = 0
        cur = 0
        for j in range(N):
            if cnt == seats:
                cur = j
                break
            if ans[j] == 0:
                cnt += 1
        for k in range(cur, N):
            if ans[k] == 0:
                ans[k] = i
                break

print(*ans)