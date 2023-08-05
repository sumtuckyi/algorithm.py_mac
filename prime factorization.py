T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    q = N
    while q != 1:
        if not q % 11:
            q //= 11
            e += 1
        elif not q % 7:
            q //= 7
            d += 1
        elif not q % 5:
            q //= 5
            c += 1
        elif not q % 3:
            q //= 3
            b += 1
        elif not q % 2:
            q //= 2
            a += 1

    print(f'#{tc} {a} {b} {c} {d} {e}')


