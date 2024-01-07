import sys

N, C = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
max_dist = arr[-1] - arr[0]
res = 0


def BS():
    global res
    start = 1
    end = max_dist
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        tof = True
        # 시작집 정하기
        f = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - f >= mid:
                # 공유기 설치
                cnt += 1
                # 기준점 바꾸기
                f = arr[i]
                # 공유기 설치 간격이 mid일 때 조건의 설치 개수를 이미 넘거나 같아진 경우 -> 설치 간격을 늘려도 됨
                if cnt >= C - 1:
                    start = mid + 1
                    # 최대 설치 간격 갱신하기
                    res = mid
                    tof = not tof
                    break
        # 설치 간격이 mid일 때 조건의 설치 개수보다 적게 설치되는 경우 -> 설치 간격 줄이기
        if tof:
            end = mid - 1

BS()
print(res)
