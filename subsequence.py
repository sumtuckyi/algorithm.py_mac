s = "vrykt"
t = "rkge"

len_s = len(s)
len_t = len(t)

idx_s = idx_t = 0  # 비교되는 문자의 인덱스
cnt = 0
while idx_t < len_t and idx_s < len_s:
    if t[idx_t] == s[idx_s]:
        idx_s += 1
        idx_t += 1
        cnt += 1
    else:
        idx_s += 1

print(cnt)