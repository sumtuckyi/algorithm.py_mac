#
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n << 8 & 0xff00) | (n >> 24 & 0xff)


def bit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)


a = 0x86
key = 0xAA

print("a     ==> ", end='')
bit_print(a)

print("a^key ==> ", end='')
a ^= key  # key와 XOR연산
bit_print(a)

print("a^=key ==> ", end='')
a ^= key
bit_print(a)
