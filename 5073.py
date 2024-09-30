while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    arr = [a, b, c]
    arr.sort()

    if arr[-1] >= arr[0] + arr[1]:
        print('Invalid')
        continue
    s = set(arr)
    if len(s) == 1:
        print('Equilateral')
    elif len(s) == 2:
        print('Isosceles')
    else:
        print('Scalene')
