import sys
from collections import deque
T = int(input())

for tc in range(1, T + 1):
    s = sys.stdin.readline()
    left = []
    right = deque()
    for token in s:
        if token.isalnum():
            left.append(token)
        elif token == '>' and right:
            left.append(right.popleft())
        elif token == '<' and left:
            right.appendleft(left.pop())
        elif token == '-' and left:
            left.pop()
    right = list(right)
    ans = left + right
    print(*ans, sep='')



