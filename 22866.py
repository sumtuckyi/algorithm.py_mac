# 현재 건물의 높이보다 큰 건물만 볼 수 있다.
# 같은 것도 못 봄
# 완전탐색? 시간초과
# 스택 이용 배열을 2회 순회

N = int(input())  # 건물의 개수
nums = list(map(int, input().split()))

# 오른쪽 카운트 - 역으로 순회
stack = []
cnt_b = [0]*N
idx = [N+1]*N # 가장 가까운 빌딩 번호

for i in range(N-1, -1, -1):
    # 스택이 차있고, 맨 위의 요소가 i보다 작거나 같은 경우
    while stack and stack[-1][0] <= nums[i]:
        stack.pop() # 모두 제거
    cnt_b[i] = len(stack) # i에서 볼 수 있는 빌딩 수 카운트
    if len(stack):
        idx[i] = stack[-1][1]  # 가장 가까운 빌딩 인덱스 저장
    stack.append((nums[i], i)) # 자기 자신을 스택에 담기

stack2 = []
for i in range(0, N): # 왼쪽 카운트
    while stack2 and stack2[-1][0] <= nums[i]:
        stack2.pop()
    cnt_b[i] += len(stack2)
    if len(stack2):
        if idx[i] == N+1:
            idx[i] = stack2[-1][1]
        else:
            if (idx[i] - i) >= (i - stack2[-1][1]):
                idx[i] = stack2[-1][1] # 거리가 더 작은 인덱스를 저장, 같으면 이번 걸로 저장
        # 오른쪽 빌딩과의 거리가 더 가까우면 갱신 안 함
    stack2.append((nums[i], i))

for cnt, i in zip(cnt_b, idx):
    if cnt > 0:
        print(cnt, i+1)
    else:
        print(0)

