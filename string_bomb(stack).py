# 폭발 문자열
# 시간초과 코드
# s = input()
# bs = input()
#
# while bs in s:
#     idx = s.find(bs)
#     first_half = s[:idx]
#     second_half = s[idx+len(bs):]
#     s = first_half + second_half
#
# print(s)
#
# result = 'FRULA' if s == '' else s
#
# print(result)

# 스택을 이용
s = str(input())  # 전체 문자열
bomb = str(input())  # 폭탄 문자열
left = []

start = 0
end = len(s) - 1  # 전체 문자열의 마지막 인덱스
while start <= end: # 스택에 전체 문자열을 하나씩 추가할 때마다 반복해서 실행(총 전체 문자열의 길이만큼)
    tof = True
    left.append(s[start])  # 스택에 차례대로 문자열을 하나씩 추가
    start += 1
    if len(left) >= len(bomb):  # 스택의 길이가 폭탄 문자열의 길이와 같거나 그보다 길면 비교
        for i in range(len(bomb)):
            if bomb[i] != left[len(left) - len(bomb) + i]:  # 폭탄 문자열의 길이 만큼 스택의 최상단 데이터와 비교
                tof = False
                break
        if tof:  # 비교 결과 스택의 마지막 데이터가 폭탄 문자열과 일치하는 경우
            for i in range(len(bomb)):
                left.pop()  # 폭탄 문자열의 길이 만큼 스택의 데이터 삭제

if len(left) == 0:
    print('FRULA')
else:
    print(*left, sep='')

