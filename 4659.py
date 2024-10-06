# 모음하나를 반드시 포함
# 모음 혹은 자음이 3개 연속으로 오면 안 된다.
# o와 e를 제외하고는 같은 글자가 두 번 연속으로 올 수 없다.

vowels = ['a', 'e', 'i', 'o', 'u']

while 1:
    pw = input()
    if pw == 'end':
        break

    # 모음 포함 여부
    has_vowel = any(char in vowels for char in pw)
    if not has_vowel:
        print(f'<{pw}> is not acceptable.')
        continue

    # 자음 혹은 모음이 3개 연속으로 오는지 확인
    is_valid = True
    if len(pw) >= 3:
        for i in range(len(pw) - 2): # 가능한 길이 3의 부분문자열의 경우
            substring = pw[i:i+3]
            if all(char in vowels for char in substring) or all(char not in vowels for char in substring):
                print(f'<{pw}> is not acceptable.')
                is_valid = False
                break
        if not is_valid:
            continue

    # 같은 글자가 두 번 연속으로 오는지 확인
    is_valid2 = True
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1] and pw[i] not in ['e', 'o']:
            print(f'<{pw}> is not acceptable.')
            is_valid2 = False
            break

    if is_valid2:
        print(f'<{pw}> is acceptable.')





