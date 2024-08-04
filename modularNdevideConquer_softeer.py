import sys

def power(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

# 입력 받기
k, p, n = map(int, sys.stdin.readline().split())

# 계산
mod = 1_000_000_007
result = (k * power(p, 10 * n, mod)) % mod

# 결과 출력
print(result)


# 백준 1629 - 분할정복, 모듈러 연산 이용
A, B, C = map(int, input().split())


def dfs(a, b, c):
    # 재귀 호출 중단 조건 - 지수가 1이면 리턴
    if b == 1:
        return a % c

    res = dfs(a, b//2, c)
    # 지수가 짝수인 경우
    if b % 2 == 0:
        return (res**2)%c
    else:
        return (res**2*a)%c


print(dfs(A, B, C))

