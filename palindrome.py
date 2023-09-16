from collections import deque

N = input()


# def is_palindrome(s):
#     chars = deque(s)
#     while len(chars) > 1:  # 문자열의 길이가 2이상인 한 반복
#         if chars.popleft() != chars.pop():
#             return False
#     return True


# def is_palindrome2(n):
#     num = n
#     reverse = 0
#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10
#     return reverse == num


# N += 1
# while True:
#     if is_palindrome2(N):
#         break
#     else:
#         N += 1


def get_palindrome(N):
    n = len(N)
    s = N[:n // 2]
    s_reversed = s[::-1]
    if n % 2 == 0:  # N의 길이가 짝수인 경우
        if int(s_reversed) > int(N[n//2:]):  # 문자열의 앞부분을 뒤집은 수가 나머지 반보다 크다면
            return s + s_reversed
        else:
            # 문자열의 앞부분에 1을 더했을 때 자릿수가 바뀌는 경우,
            pl = str(int(s) + 1)
            if len(pl) > len(s):
                return pl + pl[:n//2][::-1]
            else:
                return pl + pl[::-1]
    else:  # N의 길이가 홀수인 경우
        if int(s_reversed) > int(N[n//2+1:]):
            return N[:n//2+1] + s_reversed
        else:
            temp = str(int(N[:n // 2 + 1]) + 1)
            temp_reversed = temp[:n//2][::-1]
            return temp + temp_reversed


if len(N) == 1:
    if int(N) == 9:
        print(11)
    else:
        print(int(N)+1)
else:
    print(get_palindrome(N))
