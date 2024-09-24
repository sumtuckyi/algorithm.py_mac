N, S = map(int, input().split())

seq = list(map(int, input().split()))

# 연속된 수들의 부분합 중 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이
# 연속된 수들의 부분합 -> 슬라이딩 윈도우?

# 수열의 최댓값이 S보다 크다면 최소길이는 1이므로 1을 반환
if max(seq) >= S:
    print(1)
    exit()
if sum(seq) < S:
    print(0)
    exit()

s = e = 0
total = seq[0]

MIN_LEN = 1e10
while e < N and s <= e:
    if total >= S: # 타겟보다 부분합이 크다면
        MIN_LEN = min(e - s + 1, MIN_LEN) # 현재 부분수열의 길이 갱신
        if MIN_LEN == 2:
            break
        total -= seq[s]
        s += 1
    else: # 부분합이 더 작다면
        e += 1
        if e < N:
            total += seq[e]

print(MIN_LEN)