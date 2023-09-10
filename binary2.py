# change endian(little -> big)
def ce(n):  # n은 4바이트 이내
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)  # 24, 16, 8, 0비트씩(3바이트, 2바이트, 1바이트, 0바이트씩)
    return p
# 연산 결과 가장 상위의(앞에 있는) 바이트가 먼저 리스트에 저장됨 -> 빅 엔디안
x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))  # 리틀 엔디안
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))  # 빅 엔디안