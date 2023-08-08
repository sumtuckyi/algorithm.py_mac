# 폭발 문자열
s = input()
bs = input()

while bs in s:
    idx = s.find(bs)
    first_half = s[:idx]
    second_half = s[idx+len(bs):]
    s = first_half + second_half

print(s)

result = 'FRULA' if s == '' else s

print(result)