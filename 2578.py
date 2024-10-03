from collections import defaultdict

grid = defaultdict(list)

for i in range(5):
    row = list(input().split())
    for j in range(5):
        grid[row[j]] = [i, j]


numbers = []
for _ in range(5):
    row = list(input().split())
    numbers.extend(row)


cnt = [5]*12 # 행, 열, 우하, 우상 순서

tof = False
for idx, num in enumerate(numbers): # 하나의 숫자를 부를 때마다
    x, y = grid[num]
    cnt[x] -= 1
    cnt[y + 5] -= 1
    if x == y:
        cnt[10] -= 1
    if x + y == 4:
        cnt[11] -= 1
    lines = 0
    for i in range(12):
        if cnt[i] == 0:
            lines += 1
            if lines == 3:
                tof = True
                break
    if tof:
        print(idx + 1)
        break


