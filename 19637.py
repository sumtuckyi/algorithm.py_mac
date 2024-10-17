# 칭호의 개수는 최대 10만 개, 캐릭터의 개수도 최대 10만 개
# 캐릭터의 전투력이 주어지면 O(n)보다 낮은 시간 복잡도로 칭호를 출력할 수 있어야 함..
# 이진탐색으로 캐릭터가 속하는 범위를 판단 -> log n(십만) = 17의 시간 복잡도
# => 10만 * 17
# 전투력의 상한은 10^9(10억)
# 칭호를 입력 받은 다음 오름차순으로 정렬,,
# 어떤 칭호의 전투력 상한값이 이미 등장한 적 있는 값이면 걸러낸다.
import sys
input = sys.stdin.readline


def find_title(hp):  # 전투력을 입력받아 해당하는 칭호를 출력
    left, right = 0, len(arr) - 1
    temp_title = ''
    while left <= right:
        mid = (left + right) // 2
        if hp == arr[mid][1]:
            return arr[mid][0]
        elif hp < arr[mid][1]:
            temp_title = arr[mid][0]
            right = mid - 1
        else:
            left = mid + 1
    return temp_title


N, M = map(int, input().split())

b_set = set()
arr = []
for _ in range(N):  # 칭호와 상한을 저장
    title, bound = input().split()  # 전투력이 bound 이하이면 title
    if bound not in b_set:
        b_set.add(bound)
        arr.append([title, int(bound)])

arr.sort(key=lambda x:x[1]) # 전투력을 기준으로 오름차순으로 정렬
for _ in range(M):  # M명의 사용자의 칭호 출력
    hp = int(input())
    print(find_title(hp))