import heapq
T = int(input())


# 해당 월에 얻을 수 있는 최대 수익을 계산
def buy_or_not(wallet, bucket, profit, min_price, arr, profits): # 최종적으로 해당 월의 구매 가능한 각 경우의 수의 이익을 반환(반환하는 이익 중 최대를 선택)
    if wallet-bucket < min_price: # 가장 저렴한 종목의 가격보다 예산이 적게 남은 경우
        # print(wallet, bucket, profit)
        profits.append(profit)
        return

    for i in range(len(arr)): # 구매할 수 있는 종목의 종류
        if bucket + arr[i][0] > wallet:
            continue
        bucket += arr[i][0]
        profit += arr[i][1]
        buy_or_not(wallet, bucket, profit, min_price, arr, profits)
        bucket -= arr[i][0]
        profit -= arr[i][1]


def investment(month, wallet): # 해당 월의 투자를 결정
    global max_p
    if month > L:
        return
    arr = []
    min_price = float('inf')
    profits = []
    temp = wallet # 임시변수에 이번 달 예산 저장
    for i in range(N):
        if month != L: # 마지막 달이 아니라면
            if data[i][month+1] - data[i][month] > 0: # 수익을 얻을 수 있는 종목만 고려
                # 종목별 (가격, 차익)을 저장
                arr.append((data[i][month], data[i][month+1] - data[i][month]))
                if data[i][month] < min_price:
                    min_price = data[i][month]
    if not arr: # 수익을 얻을 수 있는 종목이 없는 경우
        investment(month + 1, wallet + A)
    else: # 수익을 얻을 수 있는 종목이 하나라도 존재하는 경우
        bucket = 0 # 주식을 사는데 사용한 금액
        profit = 0 # 이번달에 얻을 수 있는 수익
        buy_or_not(wallet, bucket, profit, min_price, arr, profits)
        this_profit = max(profits) # 이번달에 얻을 수 있는 최대 수익
        max_p += this_profit
        investment(month + 1, temp + this_profit + A)


for tc in range(1, T + 1):
    S, A = map(int, input().split())  # 시드머니, 월별 추가투자금액
    N, L = map(int, input().split())  # 종목 수, 데이터 기간
    data = [list(map(int, input().split())) for _ in range(N)]
    max_p = 0  # 누적 이익

    investment(0, S)
    print(f'#{tc} {max_p}')