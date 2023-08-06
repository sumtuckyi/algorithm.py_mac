# 탐욕 알고리즘 : 부분 문제에서 가장 최선의 선택을 해서 전체 문제를 푸는 알고리즘
# 거스름돈 문제 : 동전종류가 100원, 50원, 10원 / 가장 적은 수의 동전으로 거스름돈을 줄 수 있을까?

# 나의 풀이 - 동전의 단위가 달라지면 코드를 전부 수정해야함
change = 350
cnt = 0
new_dict = {'10': 0, '50':0, '100': 0}
n = change // 100  # 최소한의 동전 개수로 거스름돈을 줘야하므로 가장 큰 단위의 동전을 최대 몇 개 줄 수 있는지 확인
if n > 0:
    new_dict['100'] = n
    n = change % 100 # 나머지 금액
    if n // 50 >= 1:
        new_dict['50'] = 1
        new_dict['10'] = (n % 50) // 10
new_list = new_dict.values()  # 딕셔너리에서 value만 새로운 리스트에 담기
for i in new_list:  # sum() 내장함수 대신 반복문 사용
    cnt += i
print(cnt)

# 다른 풀이
def greedy(money, coins):  # coins는 리스트 타입
    coins.sort(reverse=True)  # 리스트를 내림차순으로 정렬
    change = {coin:0 for coin in coins}  # Dictionary Comprehension
    for coin in coins:  # 내림차순으로 정렬하였기 때문에 큰 단위의 동전부터 반복
        while money >= coin:
            money -= coin
            change[coin] += 1

    return change

result = greedy(380, [10, 50, 100])
print(result)