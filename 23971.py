H, W, N, M = map(int, input().split())

r = W // (M + 1)
m = 0 if W % (M + 1) == 0 else 1
r += m

c = H // (N + 1)
m = 0 if H % (N + 1) == 0 else 1
c += m

print(r*c)