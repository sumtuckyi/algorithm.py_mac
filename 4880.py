# 1은 가위, 2는 바위, 3은 보
# 몇 번째 카드를 집은 학생이 최종 승자인지 출력
# 카드의 번호가 동일한 경우 번호가 작은 학생이 승자인 걸로


def find_winner(start, end):  # 승자판별함수
    if end - start == 0:
        return start  # 학생의 번호를 리턴

    left = find_winner(start, (start+end)//2)
    right = find_winner((start+end)//2+1, end)

    return tournament(left, right)

def tournament(a, b):  # 번호를 인자로 받음
    # 시간 복잡도를 줄이기 위해 맵 사용
    condition = {
        (1, 2): b,
        (1, 3): a,
        (2, 1): a,
        (2, 3): b,
        (3, 1): b,
        (3, 2): a,
    }

    if cards[a] == cards[b]:
        return min(a, b)  # 카드에 적힌 숫자가 같으면 번호가 작은 학생이 승자
    else:
        return condition.get((cards[a], cards[b]))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = [0]*(N+1)
    row = list(map(int, input().split()))
    for i in range(1, N+1):
        cards[i] = row[i-1]
    result = find_winner(1, N)
    print(f'#{tc} {result}')