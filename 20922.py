# 투포인터 이용 배열 탐색
from collections import defaultdict

N, K = map(int, input().split())
max_len = 0
seq = list(map(int, input().split()))
count = defaultdict(int)
left = 0
for right in range(len(seq)):  # 수열의 처음부터 순회 시작
    count[seq[right]] += 1  # 빈도 저장

    while count[seq[right]] > K:
        count[seq[left]] -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)