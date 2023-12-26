# 강의의 수, cd의 수
N, M = map(int, input().split())
# 각 강의의 길이(순서가 중요)
lectors = list(map(int, input().split()))
max_value = sum(lectors)
# K의 범위
# arr = [i for i in range(max(lectors), max_value + 1)]
# 정답
K = 0


def binary_search():
    global K
    # 이분탐색 인덱스 지정
    start = max(lectors)
    end = max_value

    while start <= end: # 용량이 mid인 경우 주어진 조건을 충족하는지 판단
        cnt = 0
        vol = 0
        tof = False
        mid = (start + end) // 2
        for i in range(N):
            vol += lectors[i]
            if vol > mid:  # cd에 담은 강의 길이가 용량을 초과한 경우
                cnt += 1  # 사용한 cd 개수 플러스
                vol = lectors[i]  # 새 cd로 갱신 - 초과된 강의를 담음
            elif vol == mid: # 해당 강의를 cd에 담았을 때 정해진 용량을 딱 채운 경우
                cnt += 1
                vol = 0
            if cnt == M:  # 현재까지 사용한 cd의 개수가 M개인 경우
                if i < N-1 or (i == N-1 and vol != 0):  # 아직 담지 못한 강의가 있는 경우
                    # 용량을 늘려준다.
                    start = mid + 1
                    tof = True
                    break
        if not tof:
            end = mid - 1
            K = mid  # mid가 가능하므로 정답 갱신


binary_search()
print(K)