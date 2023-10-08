T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    the_tallest = max(trees)  # 기준 트리
    li = [] # 자라야 할 높이 저장
    for tree in trees:
        li.append(the_tallest-tree)
    # 소요일수 계산
    ones = 0
    twos = 0
    days = 0
    keep = 0  # 남는 키
    cnt = 0  # 1의 개수
    for i in li:
        if i == 0:
            continue
        # i를 3으로 나눈 나머지가 1인 경우
        if i % 3 == 1:
            ones += ((i//3)+1)
            twos += ((i//3)+1)-1
        # i를 3으로 나눈 나머지가 0인 경우
        elif i % 3 == 0:
            days += (i//3)*2
        # 나머지가 2인 경우
        else:
            days += (i//3)*2+2
            keep += 1
    # 원칙은 keep 2마다 소요일수가 1일 감소 + keep 1과 cnt 1이 상쇄되어 소요일수가 1일 감소
    ans = 0
    if cnt >= keep:
        ans = days - keep
    else:
        ans = days - cnt - (keep-cnt)//2
    print(f'#{tc} {ans}')