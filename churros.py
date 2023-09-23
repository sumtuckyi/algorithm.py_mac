# K >= N, 1 <= K <= 1,000,000, 1 <= N <= 10,000
# K가 1이면 답은 max(churros)
# K개가 나오면서 그 길이가 최대가 되어야 함
from sys import stdin
# N, K = map(int, stdin.readline().split())
# churros = []
# for _ in range(N):
#     churros.append(int(stdin.readline()))
# churros.sort()
# # K가 1인 경우
# if K == 1:
#     print(churros[-1])
#     exit()
#
# start = 1  # 가장 작은 값
# end = churros[-1]  # 가장 큰 값
# while start <= end:
#     mid = (start+end)//2
#     res = 0
#     for i in range(N):
#         res += churros[i]//mid
#     if res >= K:  # 손님이 요구하는 개수의 츄러스 제공이 가능한 경우
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

N, K = map(int, input().split())
churros = []
for _ in range(N):
    churros.append(int(input()))
churros.sort()
# K가 1인 경우
if K == 1:
    print(churros[-1])
    exit()

start = 1  # 가장 작은 값
end = churros[-1]  # 가장 큰 값
while start <= end:
    tof = False
    mid = (start+end)//2
    res = 0
    for i in range(N):
        res += churros[i]//mid
        if res >= K:  # 손님이 요구하는 개수의 츄러스 제공이 가능한 경우
            start = mid + 1
            tof = True
            break
    if not tof:
        end = mid -1


print(end)

