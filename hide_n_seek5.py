# hide_n_seek5
import sys
from collections import deque

N, K = map(int, sys.stdin.readline())
if N == K:
    print(0)
    exit()
