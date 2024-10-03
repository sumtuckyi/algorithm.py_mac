# 스택 이용
# 앞에 있는 수 중에서 최대한 큰 수를 찾는다.
# 모든 숫자를 지우는 경우는 주어지지 않는다.
# N, K = map(int, input().split())
# seq = list(map(int, input()))
#
# stack = []
# # 스택에 N - K개의 숫자만 담는다.
# # 뒤에서부터 탐색
# for i in range(N - 1, -1, -1):
#     if stack and len(stack) == (N - K): # 스택이 꽉 차있는 경우
#         if stack[-1] < seq[i]:
#             stack.pop()
#             stack.append(seq[i])
#         elif stack[-1] == seq[i]: # 같은 경우
#             if stack[-2] < seq[i]:
#
#     if not stack or len(stack) < (N - K): # 스택이 비어있거나 아직 N-K보다 짧은 경우
#         stack.append(seq[i])
#
# print(*stack)

N, K = map(int, input().split())
seq = list(map(int, input().strip()))  # 입력 받을 때 공백 제거

stack = []

# 필요한 숫자만큼만 스택에 담는다.
for i in range(N): # 앞에서부터 진행
    # 제거 조건
    # 스택이 비어있지 않고 지울 수 있는 수가 남았으며 현재 수가 스택 상단의 수보다 큰 경우
    while stack and K > 0 and stack[-1] < seq[i]:
        stack.pop() # 스택 상단의 수를 제거
        K -= 1  # 제거할 숫자를 하나 줄인다.
    stack.append(seq[i])
# 만약 뒤로갈수록 작은 수가 나온다면 스택에 수는 계속해서 쌓인다.
# 남은 K개의 수 만큼을 stack의 뒤에서 제거한다.
if K > 0:
    stack = stack[:-K]

# 최종 결과 출력
print(''.join(map(str, stack)))
