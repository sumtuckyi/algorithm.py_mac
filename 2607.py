# 같은 구성의 정의 : 같은 종류의 문자로 구성 & 같은 문자는 같은 개수만큼 존재
# 비슷한 단어의 정의 : 같은 구성 or 한 단어에서 한 문자를 더하거나, 빼거나, 바꿔서 두 단어의 구성이 같아질 수 있다.

# 최대 100개의 단어가 주어질 때,
# 첫번째 단어(기준)와 비슷한 단어가 몇 개인지 출력
from collections import defaultdict
N = int(input())
answer = 0
words = []
for _ in range(N):
    words.append(input())

# 비슷한지 판별
#1.같은 구성 - 26비트로 접근하면 & 연산 시 결과가 1
#2.한 문자를 더해서 완성 가능 - 이때 더해지는 문자는 기준 단어에만 있는 문자거나, 둘 다 있는데 기준 단어에 1개 더 많은 문자
#3.한 문자를 빼서 완성 가능 - 이때 빠지는 문자는 기준 단어에 없는 문자거나, 있는데 1개 더 많은 문자
#4.한 문자를 바꿔서 완성 가능 - 바뀐 결과인 문자는 1개 추가되고, 바뀌기 전의 문자는 1개 줄어든다.

# 기준 단어와 비교할 단어를 키를 기준으로 순회하는데, 정렬한 다음 순회..
first = words[0]
F = len(first)
first_table = defaultdict(int)
for token in first: # 기준 문자 테이블 채우기
    first_table[token] += 1

# for i in range(1, N):  # 나머지 단어와 비교
#     temp_table = defaultdict(int) # 비교할 단어의 테이블
#     for char in words[i]: # 채우기
#         temp_table[char] += 1
#
#     cnt = 0
#     for key in first_table:
#         # 먼저 같은 구성인지 확인
#         if temp_table[key] == first_table[key]:
#             cnt += 1
#     if cnt == F:  # 같은 구성
#         answer += 1
#     elif cnt == F-1:

