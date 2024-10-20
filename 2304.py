# 앞에서부터 지붕을 이어나간다고 가정
# 기준 건물보다 높은 건물이 다음에 나오는 경우
# 기준 건물높이로 수평으로 가다가 높은 건물을 만나면 따라서 올라감, 높은 건물을 기준으로 삼음
# 기준 건물보다 낮은 건물이 다음에 나오는 경우
# 지붕이 오목해지면 안 되기 때문에 다음에 나오는 건물 중 가장 높은 건물을 찾는다.
# 그 건물의 높이에 맞춰서 그 건물을 만날 때까지 수평으로 지붕을 이어 나간다.

# 그냥 구현..?
N = int(input())

arr = []
for _ in range(N):
    pos, h = map(int, input().split())  # 위치와 높이
    arr.append((pos, h))


arr.sort(key=lambda x:x[0])
taller = [None]*N
# 미리 기둥별로 해당 기둥보다 뒤에 오면서 큰 기둥 중 가장 큰 기둥의 위치 기록 - 여러 개면 가장 앞에 있는 기둥
for i in range(N-1):
    max_h = 0
    for j in range(i+1, N):
        if arr[i][1] < arr[j][1]:
            if max_h < arr[j][1]:
                max_h = arr[j][1]
                taller[i] = j

# print(taller)

total = 0  # 총 면적
i = 0
while i <= N-2:
    cur_p, cur_h = arr[i][0], arr[i][1] # 현재 기둥 좌표와 높이
    nxt_p, nxt_h = arr[i+1][0], arr[i+1][1] # 바로 다음 기둥의 좌표와 높이
    # print('cur_p:', cur_p, 'nxt_p:', nxt_p)
    if cur_h < nxt_h:
        total += (nxt_p - cur_p)*cur_h
        # print('커지는 경우', total)
        i += 1 # 바로 다음 기둥으로 넘어감
    elif cur_h == nxt_h:
        total += (nxt_p - cur_p)*cur_h
        # print('동일한 경우', total)
        i += 1 # 바로 다음 기둥으로 넘어감
    else: # 바로 다음 건물이 더 낮을 때, 내려가도 될 지를 판단
        # 다음 건물이 남은 건물 중에는 가장 높거나 같은 경우 - 내려감
        if taller[i+1] is None:
            total += (cur_h + (nxt_p - cur_p - 1)*nxt_h)
            # print('작아지지만 가장 높은 경우', total)
            i += 1  # 바로 다음 건물로 넘어감
        else: # 다음 건물보다 더 높은 건물이 남은 경우 - 내려가면 안 됨
            # print('다음 건물의 좌표', arr[taller[i + 1]][0])
            # 다음 건물보다 더 높은 건물이 현재 건물보다 높은 경우
            if arr[taller[i+1]][1] > cur_h:
                total += (arr[taller[i+1]][0] - cur_p)*cur_h # 다음 건물이 될 좌표
            # 다음 건물보다 더 높은 건물이 현재 건물보다 낮거나 같은 경우
            else:
                total += (cur_h + (arr[taller[i+1]][0] - cur_p -1)*(arr[taller[i+1]][1]))
            # print('작아지는 경우', total)
            i = taller[i+1] # 다음 기준 건물

total += arr[N-1][1]  # 마지막 기둥은 항상 그 높이만큼 더해짐
print(total)