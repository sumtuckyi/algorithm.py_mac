def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def count_total_ones(n):
    if n <= 0:
        return 0

    # n의 비트 길이
    k = n.bit_length()

    # 2^k - 1까지의 1의 개수
    total = k * (1 << (k - 1))

    # n - (2^k - 1)에 대한 처리
    n -= (1 << k) - 1
    total += n + count_total_ones(n)

    return total


# 입력 받기
A, B = map(int, input().split())

# A부터 B까지의 모든 수의 1의 개수 계산
result = count_total_ones(B) - count_total_ones(A - 1)
print(result)