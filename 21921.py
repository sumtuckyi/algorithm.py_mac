N, X = map(int, input().split())

visitors = list(map(int, input().split()))

# 길이가 X인 슬라이딩 윈도우 이용
# 방문자 수 최대인 구간이 총 몇 개인지도 카운트
s = 0
total = sum(visitors[:X])
MAX = total
cnt = 1
for e in range(X, N): # 윈도우의 끝 인덱스
    total = total - visitors[s] + visitors[e]
    # print(total)
    if total == MAX:
        cnt += 1
    elif total > MAX:
        MAX = total
        cnt = 1
    s += 1
if MAX != 0:
    print(MAX)
    print(cnt)
else:
    print('SAD')
