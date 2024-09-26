import bisect

P = int(input())

for _ in range(P):
    row = list(map(int, input().split()))
    test_case = row[0]
    students = row[1:]

    steps = 0
    line = [students[0]]  # 맨 처음 학생이 줄을 선 상태
    for i in range(1, len(students)):
        idx = bisect.bisect_left(line, students[i])
        steps += len(line) - idx
        line.insert(idx, students[i])

    print(f'{test_case} {steps}')