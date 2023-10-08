T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    the_tallest = max(trees)
    li = []
    for tree in trees:
        li.append(the_tallest-tree)
    ones = 0
    twos = 0
    for i in li:
        if i == 0:
            continue
        # 3으로 나눈 나머지가 1인 경우 -> 1과 2의 수를 최대한 맞춰 줌 (x+1, x)
        if i % 3 == 1:
            ones += ((i // 3) + 1)
            twos += (i // 3)
        # 3으로 나눈 나머지가 0인 경우 -> 1과 2의 수를 같게 맞춰줌(x, x)
        elif i % 3 == 0:
            ones += (i//3)
            twos += (i//3)
        # 3으로 나눈 나머지가 2인 경우 -> 2를 최대한 쓰고 1을 최소화 -> 어차피 최적화 단계에서 2가 1 2개로 대체됨...
        # 3으로 나눈 나머지가 0인 경우와 같이 나타내고 남는 1을 따로 표시하는게 낫나..
        else:
            ones += i % 2
            twos += i // 2
    # 1의 개수가 2의 개수보다 3 이상 많은 경우
    while ones > twos + 2:
        ones -= 2
        twos += 1
    # 1의 개수가 2의 개수보다 적은 경우
    while ones < twos:
        ones += 2
        twos -= 1
    # 정확히 1의 개수가 2의 개수보다 2개 더 많은 경우 -> 1하나를 2로 바꿔줘야함
    if ones == twos + 2:
        ones -= 1
        twos += 1
    # 반복문 종료 시 1은 2보다 1개 더 많거나 같아짐
    ans = ones + twos
    print(f'#{tc} {ans}')