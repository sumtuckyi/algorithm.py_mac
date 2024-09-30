N = int(input())

idx = 1
s, e = 1, 1
dist = 1

while 1:
    if s <= N <= e:  # 현재 구간에 속하는 경우
        print(dist)
        break

    s = e + 1
    e = s + (6 * idx) - 1
    idx += 1
    dist += 1

