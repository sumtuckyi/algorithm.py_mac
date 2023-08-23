T = int(input())


def right(idx, N):  # 해당 인덱스를 기준으로 오른쪽 탐색
    visited[idx] = 1
    k = 1
    while True:
        if idx + k <= N - 1:  # 탐색 중인 풍선이 리스트 범위 내인 경우
            if not visited[idx + k]:  # 오른쪽에 아직 터지지 않은 풍선이 있다면
                rb = scores[idx + k]
                return rb
            elif visited[idx + k]:  # 이미 터진 풍선인 경우
                k += 1  # 한 칸 더 이동
                continue  # 다음 반복으로
        else:  # 탐색 위치가 리스트를 벗어난 경우
            return 0  # 오른쪽에 남은 풍선이 없음


def left(idx, N):
    visited[idx] = 1
    k = -1
    while True:
        if idx + k > 0:  # 탐색 중인 풍선이 리스트 범위 내인 경우
            if not visited[idx + k]:  # 왼쪽에 아직 터지지 않은 풍선이 있다면
                lb = scores[idx + k]
                return lb
            elif visited[idx + k]:  # 이미 터진 풍선인 경우
                k -= 1  # 한 칸 더 이동
                continue  # 다음 반복으로
        else:  # 탐색 위치가 리스트를 벗어난 경우
            return 0  # 왼쪽에 남은 풍선이 없음

def bt(idx, total):
    global max_v, visited
    if idx == N:  # 모든 풍선을 터뜨린 경우
        if total > max_v:
            max_v = total
        return
    for i in range(N):
        if not visited[i]:  # 아직 터지지 않은 풍선이라면
            visited[i] = 1 # 선택하여
            rr = right(i, N) # 오른쪽 풍선값과
            ll = left(i, N)  # 왼쪽 풍선값을 구한 다음
            print(i, rr,ll)
            if rr and ll:  # 인접풍선이 두 개이면
                bt(idx + 1, total + (rr * ll))

                visited[i] = 0
            elif rr or ll:  # 인접풍선이 하나이면
                bt(idx + 1, total + (rr + ll))

                visited[i] = 0
            else:  # 마지막 풍선인 경우
                bt(idx + 1, total + scores[i])

                visited[i] = [0]



for tc in range(1, T  + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [0]*(N+1)
    visited2 = [0]*(N+1)
    max_v = 0
    bt(0, 0)
    print(max_v)

# def DFS(idx, now_sum):
#     global min_sum
#     if now_sum >= min_sum:
#         return
#     if idx == N:  # 모든 행을 선택한 경우
#         if min_sum > now_sum:  # 현재합이 최소합보다 작으면 갱신
#             min_sum = now_sum
#         return
#     for i in range(N):
#         if not used[i]:  # 아직 선택하지 않은 열이라면
#             used[i] = 1  # 선택하여
#             DFS(idx+1, now_sum+arr[idx][i])  # 최솟값 여부 판단(현재 level(행)에서 아직 선택되지 않은 열에 한해서 선택)
#             used[i] = 0  # 원상복구(백트래킹)
