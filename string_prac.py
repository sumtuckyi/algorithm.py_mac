def strlen(arr):
    i = 0
    cnt = 0
    while True:
        if arr[i] != '₩0':
            cnt += 1
            i += 1
        else:
            break
    return cnt


a = ['a', 'b', 'c', '₩0']
print(strlen(a))

def string_reversal(s):
    new_str = ''
    for i in range(len(s) - 1, -1, -1):
        new_str += s[i]
    return new_str

print(string_reversal('hello~!'))

# def string_reversal2(s):
#     for i in range(len(s) // 2):
#         pass
#
# print(string_reversal2('algorithm'))

def atoi(s):
    for i in range(len(s)):
        pass



