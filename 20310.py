S = input()

# 0과 1의 개수 세기
one, zero = 0, 0
for token in S:
    if token == '0':
        zero += 1
    else:
        one += 1

# 앞에서부터 절반의 1 제거하기
S_list = list(S)
cnt = 0  # 삭제할 1의 개수
i = 0
while i < len(S_list) and cnt < one//2:
    if S_list[i] == '1':
        S_list.pop(i)  # i번째 인덱스의 값을 삭제
        cnt += 1
    else:
        i += 1

# 뒤에서부터 절반의 0 제거하기
cnt = 0  # 삭제할 0의 개수
i = len(S_list) - 1  # 뒤에서부터 삭제
while i >= 0 and cnt < zero//2:
    if S_list[i] == '0':
        S_list.pop(i)
        cnt += 1
    i -= 1

print(''.join(S_list))