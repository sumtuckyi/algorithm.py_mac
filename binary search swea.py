# 찾는 수가 arr에 들어있을 때, 이 수를 찾기 위해 이진탐색을 수행할 경우
# 왼쪽 구간과 오른쪽 구간을 모두 탐색하여 찾게되는 경우를 카운트하여 출력
# 단, mid=target으로 찾게되는 경우도 포함한다.
# 연달아 같은 방향의 부분집합을 탐색구간으로 정하는 경우 바로 -1을 리턴하도록
# N,M은 모두 양의 정수임
def binary_search_recursive(low, high, target):
    global l, r, pre
    # 재귀호출을 반복하지 않을 조건
    # target값이 존재하지 않는 경우
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == target:
        return True
    # 해당 구간에서 찾는 값이 중간값보다 큰 경우
    elif arr[mid] < target:
        # 이전 탐색구간이 오른쪽이었다면
        if pre == 'r':
            return -1
        # 최근 탐색구간 설정
        pre = 'r'
        return binary_search_recursive(mid + 1, high, target)
    # target이 중간값보다 작은 경우
    else:
        if pre == 'l':
            return -1
        # 중간값 기준으로 왼쪽 부분집합 탐색
        pre = 'l'
        return binary_search_recursive(low, mid - 1, target)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    m = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    # 바로 이전의 탐색구간이 오른쪽인지 왼쪽인지
    for i in m:
        pre = ''
        # 타겟을 찾은 경우
        if binary_search_recursive(0, N-1, i) != -1:
            cnt += 1
    print(f'#{tc} {cnt}')