# 연속한 부분의 합이 M으로 나누어 떨어지는 구간의 개수 구하기

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
S = [0] * N
C = [0] * M  # 구간합의 나머지를 카운트하여 결과를 저장할 리스트
# 구간 합 구하기
for i in range(N):
    if i == 0:
        S[i] = arr[i]
    else:
        S[i] = S[i - 1] + arr[i]
# M으로 나눈 나머지로 구간합 배열의 요소 바꾸기
for i in range(N):
    S[i] = S[i] % 3
    if S[i] == 0:
        cnt += 1
    C[S[i]] += 1
# 구간의 개수 구하기
for i in range(M):
    if C[i] > 1:
        cnt += (C[i] * (C[i] - 1)) // 2


# for i in range(N):
#     for j in range(i + 1, N):
#         if S[j] == S[i]:
#             cnt += 1

print(cnt)




# print(prefix_sum)
# # 가능한 모든 구간에 대해 M으로 나누어 떨어지는지 확인
# for i in range(1, N + 1):
#     for j in range(i):
#         if not ((prefix_sum[i] - prefix_sum[j]) % M):
#             cnt += 1
