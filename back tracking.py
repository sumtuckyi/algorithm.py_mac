n, m = map(int, input().split())
answer = []

def back_tracking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if i in answer:  # 중복을 허용하지 않음
            continue
        answer.append(i)
        back_tracking(depth + 1)
        answer.pop()

back_tracking(0)