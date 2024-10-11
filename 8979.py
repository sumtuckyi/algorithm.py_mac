N, K = map(int, input().split())

rank = []
for _ in range(N):
    con, g, s, b = map(int, input().split())
    rank.append((con, g, s, b))

# 정렬은 해결
rank.sort(key= lambda x: (x[1], x[2], x[3]), reverse=True)

# rank를 순회하면서 K국가의 등수 찾기
res = [0]*(N + 1)

cur_rank = 1
prev = rank[0][1:]  # 1등 국가의 성적
res[rank[0][0]] = cur_rank  # 1등 국가 기록
tied = 1
for i in range(1, N):
    # 같은 조합이 몇 번 등장하는지 확인
    c, g, s, b = rank[i] # 현재 국가의 성적
    if (g, s, b) == prev: # 이전 국가의 성적과 동일하면
        res[c] = cur_rank
        tied += 1
    else: # 다르면
        cur_rank += tied
        res[c] = cur_rank
        prev = (g, s, b)  # 다음 국가와 비교할 조합을 갱신
        tied = 1 # 초기화


print(res[K])