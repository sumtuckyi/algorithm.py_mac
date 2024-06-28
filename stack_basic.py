# sent = input()
# bomb = input()
#
# stack = []
# b_len = len(bomb)
#
# for char in sent:
#     stack.append(char)
#     if len(stack) >= b_len and ''.join(stack[-b_len:]) == bomb:
#         del stack[-b_len:]
#
# if not stack:
#     print('FRULA')
# else:
#     print(''.join(stack))
#
#
#

# 폭발 문자열의 마지막 문자열이 등장한 경우에만 폭발 문자열의 길이만큼 스택에서 꺼내어 비교하여 처리한다.
sent = input()
bomb = input()

stack = []
len_b = len(bomb)

for char in sent:
    stack.append(char)
    if char == bomb[-1] and len(stack) >= len_b:
        # print("발견!", stack[-len_b:])
        if ''.join(stack[-len_b:]) == bomb:
            for _ in range(len_b):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))

# del보다 pop()사용이 더 빠르다..