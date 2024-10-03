# 라인 개수 세기
from collections import defaultdict


def count_lines(case):
    grid = []
    # 2차원 배열로 만들기
    for i in range(3):
        grid.append(case[i*3:i*3 + 3])

    x_lines = 0
    o_lines = 0
    # X 라인 세기
    for i in range(3): # 가로줄
        if grid[i][0] == 'X' and grid[i][1] == 'X' and grid[i][2] == 'X':
            x_lines += 1
    for i in range(3): # 세로줄
        if grid[0][i] == 'X' and grid[1][i] == 'X' and grid[2][i] == 'X':
            x_lines += 1
    if grid[1][1] == 'X' and grid[2][2] == 'X' and grid[0][0] == 'X':
        x_lines += 1
    if grid[2][0] == 'X' and grid[1][1] == 'X' and grid[0][2] == 'X':
        x_lines += 1
    # O 라인 세기
    for i in range(3): # 가로줄
        if grid[i][0] == 'O' and grid[i][1] == 'O' and grid[i][2] == 'O':
            o_lines += 1
    for i in range(3): # 세로줄
        if grid[0][i] == 'O' and grid[1][i] == 'O' and grid[2][i] == 'O':
            o_lines += 1
    if grid[1][1] == 'O' and grid[2][2] == 'O' and grid[0][0] == 'O':
        o_lines += 1
    if grid[2][0] == 'O' and grid[1][1] == 'O' and grid[0][2] == 'O':
        o_lines += 1

    return x_lines, o_lines


while 1:
    case = input()
    if case == 'end':
        break
    # 문자 수 세기
    char_dict = defaultdict(int)
    for token in case:
        char_dict[token] += 1
    x_lines, o_lines = count_lines(case)
    if x_lines == 1 and o_lines == 0:
        if char_dict['X'] == char_dict['O'] + 1:
            print('valid')
        else:
            print('invalid')
    elif x_lines == 0 and o_lines == 1:
        if char_dict['X'] == char_dict['O']:
            print('valid')
        else:
            print('invalid')
    elif x_lines == 0 and o_lines == 0:
        if char_dict['X'] == 5 and char_dict['O'] == 4:
            print('valid')
        else:
            print('invalid')
    elif x_lines == 2 and char_dict['X'] == 5 and char_dict['O'] == 4:
        print('valid')
    else:
        print('invalid')

    # print(x_lines, o_lines)