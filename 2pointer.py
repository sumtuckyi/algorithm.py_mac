from collections import defaultdict
T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    dishes = list(map(int, input().split()))
    ans = 'YES'
    dup_check = [0] * (N+1)
    start = 0
    end = 2 * R
    d = defaultdict(int)
    # 첫번째 반복
    for i in range(start, end+1):
        d[dishes[i]] += 1
        for v in d.values():
            if v > 2:
                ans = 'NO'
    while start <= N-1:
        d[dishes[start]] -= 1
        start += 1
        end += 1
        d[dishes[end%N]] += 1
        for v in d.values():
            if v > 2:
                ans = 'NO'
                break

    print(f'#{tc} {ans}')