from collections import defaultdict


N, M = map(int, input().split())

words_dict = defaultdict(int)
# 글자수로 필터링
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    words_dict[word] += 1

# 정렬
words_arr = [[] for _ in range(100_000 + 1)]
for key, val in words_dict.items():
    words_arr[val].append((key, val)) # 빈도 기준으로 그룹화

for group in words_arr:
    group.sort() # 사전순
    group.sort(key= lambda x: len(x[0]), reverse= True)  # 단어의 길이 기준으로 정렬

for arr in words_arr[::-1]:
    if len(arr) == 0:
        continue
    for word, freq in arr:
        print(word)






