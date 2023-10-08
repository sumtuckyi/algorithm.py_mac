T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    the_tallest = max(trees)
    li = []
    cnt = 0  # 1의 개수
    sur = 0  # 남는 높이
    for tree in trees:
        li.append(the_tallest-tree)
        if tree == 1:
            cnt += 1
    ones = twos = 0
    for i in li:
        if i == 0:
            continue
        # 3으로 나눈 나머지가 1인 경우(1은 제외) -> 1과 2의 수를 최대한 맞춰 줌 (x+1, x)
        if i % 3 == 1 and i != 1:
            ones += ((i // 3) + 1)
            twos += (i // 3)
        # 3으로 나눈 나머지가 0인 경우 -> 1과 2의 수를 같게 맞춰줌(x, x)
        elif i % 3 == 0:
            ones += (i//3)
            twos += (i//3)
        # 3으로 나눈 나머지가 2인 경우 -> 2를 최대한 쓰고 1을 최소화 -> 어차피 최적화 단계에서 2가 1 2개로 대체됨...
        # 3으로 나눈 나머지가 0인 경우와 같이 나타내고 남는 1을 따로 표시하는게 낫나..
        else:
            ones += (i // 3)
            twos += (i // 3)
            sur += 1
    # 소요일수 최소화 -> 1이 존재할 때 문제 발생

    ans = ones + twos
    print(f'#{tc} {ans}')