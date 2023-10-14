import sys
T = int(input())

for tc in range(1, T + 1):
    s = sys.stdin.readline()
    pw = []
    i = 0  # 스택의 0번째 인덱스의 앞에 커서가 위치(입력란의 맨 앞에 커서가 위치한 경우)
    for token in s:
        if token.isalnum():
            if i == len(pw):  # 커서의 위치가 줄의 마지막인 경우
                pw.append(token)
                i += 1
            else:
                temp = pw[i:]  # 삽입될 문자의 뒤에 올 문자열
                temp2 = pw[:i]  # 삽입될 문자의 앞에 올 문자열
                temp2.append(token)  # 새로운 문자를 삽입
                pw = temp2 + temp
                # pw.insert(i, token)
                i += 1    # 커서 위치 설정
        elif token == '<' and i != 0:  # 현재 커서 앞에 최소 1개의 문자가 존재
            i -= 1
        elif token == '>':  # 현재 커서 뒤에 최소 1개의 문자가 존재
            if i != len(pw) and pw:
                i += 1
        else:  # token이 '-'이면
            if i != 0 and pw:  # 현재 커서의 왼쪽에 문자나 숫자가 있는 경우
                temp = pw[i:]
                temp2 = pw[:i]
                temp2.pop()
                pw = temp2 + temp
                # pw.pop(i-1)
                i -= 1  # 비밀번호가 한 자리 삭제되었으므로 커서 위치 이동
    print(*pw, sep='')


