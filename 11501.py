T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    total = 0
    for i in range(N - 2, -1, -1):
        if price[i] < max_price:
            total += (max_price - price[i])
        if price[i] > max_price:
            max_price = price[i]
    print(total)