def check(data):  # 중복카드가 있는지 확인
    for i in range(n//3):  # 카드의 수만큼 확인
        if data[i*3:i*3+3] in dup:
            return 0
        else:
            dup.append(data[i*3:i*3+3])
    return 1


T = int(input())
for tc in range(1, T + 1):
    cards = input()
    n = len(cards)
    dup = []
    d = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    if check(cards):  # 중복 카드가 없으면
        for card in dup:
            d[card[0]] += 1
        print(f'#{tc}', 13-d['S'], 13-d['D'], 13-d['H'], 13-d['C'])
    else:
        print(f'#{tc} ERROR')