N = int(input())

arr = []
for _ in range(N):
    pos, h = map(int, input().split())  # 위치와 높이
    arr.append((pos, h))

arr.sort(key=lambda x:x[0])

area = 0
stack = [] # 단조감소스택으로 사용
for cur_pos, cur_h in arr:
    while stack and stack[-1][1] <= cur_h:  # 스택 최상단 값보다 크면
        p, h = stack.pop()
        if not stack: # 스택의 마지막 요소이면
            area += (cur_pos - p)*h
        else: # 스택에 더 있으면
            pass

    stack.append((cur_pos, cur_h))
    # print(stack, area)
stack = stack[::-1]
tallest_p, tallest_h = stack.pop()
area += tallest_h
prev_p = tallest_p
# print(area)
# 스택에 남아있는 요소를 계산한다. - 무조건 내림차순
while stack:
    pos, h = stack.pop()
    area += (pos - prev_p)*h
    prev_p = pos

print(area)