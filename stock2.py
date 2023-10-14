# 수익이 나는 경우에만 종목별 가격, 차익 저장(arr)

arr = [(100, 5), (150, 3), (200, 2), (120, 6), (80, 1)]
arr2 = [5, 3, 2, 4, 6] # 구매 가능한 최대 개수 -> 6*4*3*5*7
wallet = 500 # 해당 월의 예산
temp = wallet #구매 결정을 하기 전의 예산을 저장
min_price = 80
profits = []

bucket = 0  # 구매하기로 결정한 종목을 구입하는데 필요한 금액
profit = 0
# 예산이 존재하는 한 구매 결정을 반복
def buy_or_not(wallet): # 최종적으로 해당 월의 구매 가능한 각 경우의 수의 이익을 반환(반환하는 이익 중 최대를 선택)
    global bucket, profit
    if wallet-bucket < min_price: # 가장 저렴한 종목의 가격보다 예산이 적게 남은 경우
        profits.append(profit)
        return

    for i in range(len(arr)): # 구매할 수 있는 종목의 종류
        if bucket + arr[i][0] > wallet:
            continue
        bucket += arr[i][0] # 해당 종목을 구매하는 경우
        profit += arr[i][1]
        buy_or_not(wallet)
        bucket -= arr[i][0]
        profit -= arr[i][1]

buy_or_not(wallet)
print(profits)

