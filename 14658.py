N, M, L, K = map(int, input().split()) # 가로, 세로, 한 변의 길이, 별의 개수
# 보호망의 크기는 별이 떨어지는 구역의 크기보다 클 수도 작을 수도 있다. 최대 넓이는 100억
# 별의 수는 최대 100개
# 완전탐색으로 모든 가능한 보호망의 위치에 따라 막을 수 있는 별의 개수를 세는 것은 비효율적..
# 별의 수가 적은 것으로 보아 별 기준으로 판단?

# 도출해야하는 답은 보호망으로 최대한 많은 별을 감쌀 때, 감싸지지 않고 남는 별의 개수니까 답은 1에서 K이다.
star = []
for _ in range(K):
    x, y = map(int, input().split())
    star.append((x, y))

MAX = -1
# 모든 가능한 서로 다른 별의 쌍에 대해 하나의 별의 x좌표와 나머지 별의 y좌표를 기준으로 하는 1사분면만 고려한다. -> 총 9900가지
for i in range(K): # 기준 별
    cur_x = star[i][0]
    for j in range(K): # 나머지 별
        cnt = 0
        cur_y = star[j][1]
        nx, ny = cur_x + L, cur_y + L
        for s in range(K): # 모든 별에 대해
            if cur_x <= star[s][0] <= nx and cur_y <= star[s][1] <= ny:
                cnt += 1
        MAX = max(cnt, MAX)

print(K - MAX)
