N, K = map(int, input().split())
holes = list(map(int, input().split()))

max_len = holes[-1] + 1
res = [0]

def BS():
    s = 1
    e = max_len
    while s <= e:
        p = 0
        mid = (s + e) // 2
        tof = True
        f = holes[0]

        for i in range(1, len(holes)):
            if holes[i] - f + 1 >= mid:
                p += 1
                if holes[i] - f == mid: # 이번 구멍까지 보수 가능
                    if i + 1 <= N - 1: # 다음 구멍의 위치가 존재한다면
                        f = holes[i + 1]
                        if p >= K: # 조건을 만족 못 함- 패치 길이 늘려야함
                            s = mid + 1
                            tof = False
                            break
                    else: # 이번이 마지막 구멍
                        if p == K:
                            res[0] = mid
                            tof = False
                            break
                else:  # 이번 구멍을 보수하려면 새 패치가 필요
                    f = holes[i]
                    if p == K:  # 조건을 만족 못함
                        s = mid + 1
                        tof = False
                        break
        if tof:
            res[0] = mid
            # print(f'mid 갱신 = {mid}')
            e = mid - 1

BS()
print(res[0])
