import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
arr.sort()

def search(s, e, t):
    if s > e:
        print(0)
        return

    mid = (s + e) // 2
    if arr[mid] == t:
        print(1)
        return
    elif arr[mid] > t:
        search(s, mid - 1, t)
    elif arr[mid] < t:
        search(mid + 1, e, t)

for i in targets:
    search(0, N - 1, i)