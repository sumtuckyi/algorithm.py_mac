# 대소문자는 아스키코드로 32차이
S = input()

cnt = [0]*26
for token in S:
    x = ord(token)
    if x >= 97: # 소문자이면
        cnt[(x-32) % 65] += 1
    else:
        cnt[x % 65] += 1
MAX = -1e10
count = 0
idx = None
for i in range(26):
    if cnt[i] > MAX:
        MAX = cnt[i]
        idx = i
        count = 1
    elif cnt[i] == MAX:
        count += 1

if count > 1:
    print('?')
else:
    print(chr(idx + 65))