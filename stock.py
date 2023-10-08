import heapq
T = int(input())

def investment(month, wallet): # 해당 월의 투자를 결정
    global max_p
    print('month', month)
    # (L+1)회 매수여부 판단 - i달마다 각 종목의 i개월 가격과 i+1개월 가격을 비교
    if month > L:
        print(wallet)
        return
    # 매월 종목별로 투자 수익을 비교하여 가장 큰 차익으로 매도 할 수 있는 종목을 최대한 매수
    pq = []
    for i in range(N):
        if month != L:  # 마지막 달에는 매수를 하지 않으므로 차익을 비교할 수 없음
            # 종목별 주당 차익과 주당 가격을 저장(양수인 경우만)
            if data[i][month+1] - data[i][month] > 0:
                # 종목별 가격 당 차익을 최대힙에 저장
                print(i, month)
                heapq.heappush(pq, (-((data[i][month+1] - data[i][month])/data[i][month]), data[i][month], data[i][month+1] - data[i][month]))
    # 어떤 주식을 매수해도 이익을 볼 수 없는 경우(최대힙이 빈 경우) -> 다음 달 투자 여부 결정
    if not pq:
        investment(month + 1, wallet + A)
    # 매수하면 이익을 얻을 수 있는 종목이 하나라도 존재하는 경우
    else:
        temp = wallet
        print('pq', pq)
        profit = 0
        while pq:
            # 우선순위가 높은 종목부터 구입
            priority, price, sub = heapq.heappop(pq)
            print(priority, price, sub, wallet)
            if wallet//price == 0: # 현재 잔고로 어떠한 주식도 살 수 없는 경우
                break
            profit += (sub)*(wallet//price)  # 다음달의 잔고 증가분
            max_p += (sub)*(wallet//price)
            wallet -= (wallet//price)*price

        print('monthly profit', profit, max_p)
        investment(month + 1, temp + profit + A)


for tc in range(1, T + 1):
    S, A = map(int, input().split())  # 시드머니, 월별 추가투자금액
    N, L = map(int, input().split())  # 종목 수, 데이터 기간
    data = [list(map(int, input().split())) for _ in range(N)]
    max_p = 0  # 누적 이익

    investment(0, S)
    print(f'#{tc} {max_p}')