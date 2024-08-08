import sys

def power(base, exponent, mod): # base는 밑, exponent는 지수
    result = 1
    base = base % mod # base가 mod보다 작거나 같게 만든다. 이 문제에서는 base < mod
    while exponent > 0:
        if exponent % 2 == 1: # 지수가 홀수이면
            result = (result * base) % mod # base를 한 번 더 곱해준다.
        exponent = exponent // 2 # 지수를 2로 나누어 크기를 줄인다.
        base = (base * base) % mod # base를 제곱한다. 이때 수가 커지지 않고 mod보다 작도록 연산한다.
    return result

# 입력 받기
# 1 ≤ K ≤ 10**8 인 정수
# 1 ≤ P ≤ 10**8 인 정수
# 1 ≤ N ≤ 10**16 인 정수
k, p, n = map(int, sys.stdin.readline().split())

# 계산
mod = 1_000_000_007
result = (k * power(p, 10 * n, mod)) % mod

# 결과 출력
print(result)


# 백준 1629 - 분할정복, 모듈러 연산 이용, 반복문 대신 재귀로 구현
# A가 밑, B가 지수, C가 나누는 값
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

