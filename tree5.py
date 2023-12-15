T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    the_tallest = max(trees)  # 기준 트리
    li = []  # 자라야 할 높이 저장
    ans = 0
    cnt_two = 0
    cnt_one = 0

    for tree in trees:
        sub = the_tallest - tree
        li.append(sub)
        cnt_two += sub // 2
        cnt_one += sub % 2

    print('(2의 개수): ', cnt_two, '(1의 개수): ', cnt_one)
    # 2의 개수 = 1의 개수 : (1의 개수*2일)
    if cnt_two == cnt_one:
        ans = cnt_one*2
    # 2의 개수 < 1의 개수 : (1의 개수*2일) - 1
    elif cnt_two < cnt_one:
        ans = (cnt_one*2) - 1
    else:
        print('2의 개수가 더 많은 경우')
        diff = cnt_two - cnt_one
    # 2의 개수 > 1의 개수 : (cnt_two - cnt_one) // 3 = 1 or 2 or 3일텐데 ->
        # 1인 경우에는 1을 하나 더 추가하고 => (2의 개수)*2
        if diff % 3 == 1: # 예를 들어 (10, 3) -> (9, 5) -> (8, 7) ->
            cnt_two -= (diff // 3)
            cnt_one += (diff // 3)*2
            ans = cnt_two*2
        # 2인 경우에는 2 하나를 1로 쪼개고 => (2의 개수)+(1의 개수)
        elif diff % 3 == 2:  # 예를 들어 (10, 2) -> (9, 4) -> (8, 6) -> (7, 8)
            cnt_two -= (diff // 3) + 1
            cnt_one += ((diff // 3) + 1)*2
            ans = cnt_one + cnt_two
        # 3인 경우에는 2 하나를 1로 쪼갠다 => (2의 개수)*2
        else:  # 예를 들어 (10, 4) -> (9, 6) -> (8, 8)
            cnt_two -= (diff // 3)
            cnt_one += (diff // 3)*2
            ans = cnt_two*2

    print(ans)
