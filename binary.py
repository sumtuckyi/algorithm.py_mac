# 인자로 받은 수를 2진수로 나타내었을 때 마지막 8비트를 출력하는 함수
def bit_print(i):
    output = ""
    for j in range(7, -1, -1):  # i의 0번째부터 7번째자리 비트까지 0인지 검사
        output += "1" if i & (1 << j) else "0"
    print(output, end=' ')


a = 0xff  # 16진수
x = 0x01020304
c = 0b101  # 2진수
d = 255  # 10진수
e = 0o77  # 8진수
print("%d = " % a, end='')  # 출력 포맷 지정
bit_print(a)
print()
print("%d = " % x, end='')
bit_print(x)
print()
print("%d = " % d, end='')
bit_print(d)
print()
print("%d = " % e, end='')
bit_print(e)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    # x를 뒤에서부터 8비트(1byte) 단위로 11111111과 &연산을 수행
    # x를 2진수로 나타낸 것을 뒤에서부터 8비트씩 나누어서 출력
    bit_print((x >> i*8) & 0xff)  # 0xff는 10진수 255를 16진수로 나타낸 것


