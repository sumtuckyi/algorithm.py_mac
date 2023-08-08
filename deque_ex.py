from collections import deque

N, L = map(int, input().split())
now = list(map(int, input().split()))

mydeque = deque()

for i in range(N):  # 데이터의 개수 만큼 반복
    # 덱의 가장 마지막 데이터와 덱에 추가하려는 데이터의 값을 비교
    while mydeque and mydeque[-1][0] > now[i]:  # 덱이 비어있지 않으면서 덱의 마지막 데이터의 값이 현재 데이터보다 클 때
        mydeque.pop()
    mydeque.append((now[i], i))  # 현재 데이터의 값과 인덱스 순서로 덱에 추가
    if mydeque[0][1] <= i - L:  # 덱의 가장 앞에 있는 데이터의 인덱스가 현재 데이터의 윈도우 범위 밖인 경우
        mydeque.popleft()
    print(mydeque[0][0], end=' ')

'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6
'''