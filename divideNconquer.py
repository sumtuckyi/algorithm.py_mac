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

