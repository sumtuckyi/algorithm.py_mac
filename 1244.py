N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    s, n = map(int, input().split())
    if s == 1:
        # 스위치 인덱스(1부터 시작)가 n의 배수이면 상태를 바꾼다.
        for i in range(N):
            if (i + 1) % n == 0:
                switch[i] ^= 1
    else:
        # n번 스위치를 중심으로 대칭인 최장 구간의 상태를 모두 반대로 바꾼다
        # 대칭인 구간 찾기
        cur = l = r = n - 1
        while True:
            nl, nr = l - 1, r + 1
            if nl < 0 or nr > N - 1:  # 범위가 인덱스 범위를 벗어나면 중단
                break
            if switch[nl:cur] != switch[cur + 1: nr + 1][::-1]:  # 현재 구간이 대칭이 아니면 중단
                break
            l, r = nl, nr
        for i in range(l, r + 1):
            switch[i] ^= 1

for i in range(0, len(switch), 20):
    print(' '.join(map(str, switch[i:i + 20])))