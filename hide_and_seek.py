import sys
from collections import deque

# 경로를 출력해야하므로 큐에 위치가 아닌 경로를 추가
N, K = map(int, sys.stdin.readline().split())
# 시작부터 둘의 위치가 같은 경우
if N == K:
    print(0)
    print(N)
    exit()
# 수빈이가 더 뒤에 있는 경우
elif N > K:
    print(N-K)
    for i in range(N, -1, -1):
        print(i, end=' ')
    exit()
# 수빈이가 더 앞에 있는 경우
else:
    q = deque()  # 수빈이의 가능한 위치
    q.append([N])
    ans = []
    visited = [-1 for _ in range(100_001)]
    visited[N] = 0  # 수빈이의 초기 위치 방문 처리 - 출발점이므로 0초 소요
    while True:
        cur_path = q.popleft()  # 큐에서 꺼낸 값은 리스트 형식
        cur = cur_path[-1]  # 경로의 마지막 위치
        # 다음 위치를 계산
        # 다음 이동 시 동생을 만나는 경우
        if (cur - 1 == K) or (cur + 1 == K) or (cur * 2 == K):
            temp = cur_path.copy()
            temp.append(K)
            ans = temp
            break
        # 동생을 만나지 못하는 경우 - 중복이면 넘어가고 중복이 아니면 큐에 추가
        if cur * 2 != K and cur * 2 <= 100_000:
            if not visited[cur * 2]:  # 다음 위치가 동생의 위치가 아니지만 아직 방문한 적이 없는 경우
                visited[cur * 2] = 1
                temp_sub = cur_path.copy()
                temp_sub.append(cur * 2)
                q.append(temp_sub)
        if cur + 1 != K and cur + 1 <= 100_000:
            if not visited[cur + 1]:
                visited[cur + 1] = 1
                tem_pl = cur_path.copy()
                tem_pl.append(cur + 1)
                q.append(tem_pl)
        if cur - 1 != K and cur - 1 >= 0:
            if not visited[cur - 1]:
                visited[cur - 1] = 1
                tem_mul = cur_path.copy()
                tem_mul.append(cur - 1)
                q.append(tem_mul)

    print(len(ans) - 1)
    print(*ans)



