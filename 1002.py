import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 답은 0(만나지 않음), 1(접함), 2(2개의 점에서 교차)만 가능
    # x1**2 + y1**2 == r1**2
    # x2**2 + y2**2 == r2**2
    #1과 2의 거리를 구한다. r1 + r2와 비교한다.
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # -1인 경우(동일한 원)
    if dist == 0 and r1 == r2:
        print(-1)
    # 2인 경우
    elif abs(r1 - r2) < dist < r1 + r2:
        print(2)
    # 1인 경우(외접/내접)
    elif (dist == r1 + r2) or (dist == abs(r1 - r2)):  # 여기서 두번째 조건이 동일한 원인 경우에도 참이 됨.
        print(1)
    # 0인 경우
    else:
        print(0)
