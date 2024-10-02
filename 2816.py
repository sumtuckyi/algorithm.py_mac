# 초기에 화살표는 첫번째 채널을 가리킨다.
# 특정 채널을 각각 1, 2 위치에 오게 하기 위한 방법을 출력(길이가 500보다 작아야 함)
# 전체 채널은 최대 100개

N = int(input())
kbs = [0, 0]
for i in range(N):
    c = input()
    if c == 'KBS1':
        kbs[0] = i
    if c == 'KBS2':
        kbs[1] = i

ans = ''
ans += kbs[0]*'1' + '4'*kbs[0] # KBS1을 찾아서 이동시키기
# KBS2의 위치 추정
if kbs[0] > kbs[1]: # 최초에 kbs1이 더 아래에 있던 경우
    kbs[1] += 1  # kbs1이 이동하는 과정에서 kbs2를 만나 인덱스가 바뀜
if kbs[1] != 1:
    ans += '1'*kbs[1] + '4'*(kbs[1] - 1)

print(ans)