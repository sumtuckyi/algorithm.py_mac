import sys

input = sys.stdin.readline
N, G = input().split() # 게임신청 횟수, 게임의 종류

genre = {
    "Y": 2,
    "F": 3,
    "O": 4
}
s = set()
for _ in range(int(N)):
    player = input()
    s.add(player)

print(len(s) // (genre[G] - 1))




