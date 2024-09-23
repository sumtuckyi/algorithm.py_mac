# 비트마스킹 이용하여 집합 연산 구현
import sys
input = sys.stdin.readline

M = int(input())
s = 0  # 처음엔 공집합
ALL_SET = (1 << 20) - 1

for _ in range(M):
    row = list(input().split())
    q = row[0]

    if q == 'add':
        s |= (1 << (int(row[1])-1))
    elif q == 'remove':
        s &= ~(1 << (int(row[1])-1))
    elif q == 'check':
        sys.stdout.write('1\n' if s & (1 << (int(row[1])-1)) else '0\n')
    elif q == 'toggle':
        s ^= (1 << (int(row[1])-1))
    elif q == 'all':
        s = ALL_SET
    else:
        s = 0

# 원소는 1부터 20까지만 존재 - 처음에 집합 초기화
# add - 원소 추가 : x번 비트만 1로 바꾸기(|연산)
# remove - 원소 제거 : x번 비트만 0으로 바꾸기(&연산)
# check - 원소 유무 확인 : (1<<x)와 기존집합을 &연산한 것이 (1<<x)와 같은지 확인한다.
# toggle - 있으면 제거하고 없으면 추가(^연산)
# all - 모든 원소를 포함한 집합으로 바꾼다.
# empty - 공집합으로 바꾼다.