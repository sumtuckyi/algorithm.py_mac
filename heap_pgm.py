import heapq
import itertools


def solution(k, n, reqs):
    # k는 유형이고, 1 <= k <= 5
    # n은 상담원의 수이고, k <= n <= 20
    # 참가자는 최소 3명에서 최대 300명
    # 각 유형마다 적어도 한 명의 상담원을 둔다.
    m = n - k
    # 기다린 시간의 총합을 최적화(최소화)
    # print("k ", k)
    # 일단 reqs를 유형별로 구분
    # reqs는 상담을 요청한 시간이 이른 순으로 정렬되어 있다.
    req = [[] for _ in range(k + 1)]
    # 참가자를 유형별로 분리
    for a, b, c in reqs:
        idx = c
        req[idx].append([a, b])
    # print(req)
    time = [[] for _ in range(k + 1)]
    # print("time 배열: ", time)
    # 유형별 & 상담사 인원별 대기시간 계산
    for i in range(1, k + 1):  # 유형 i의
        # print(f'유형 {i}')
        for j in range(1, m + 2):  # 상담인원이 j명일 때
            # print(f'상담원 {j}명')
            # 상담 종료 시각을 기록할 배열과 대기시간 기록
            done = []  # 최소힙 사용해야..
            for _ in range(j):
                heapq.heappush(done, 0)  # 최초에 종료시각은 0
            t = 0
            for p in req[i]:  # 모든 참가자를 탐색해서 대기시간 계산
                a, d = p[0], p[1]  # 도착 시각과 소요시간
                x = heapq.heappop(done)  # 가장 이른 종료시각
                # print(x)
                if x <= a:  # 도착시간보다 종료시각이 이른 경우
                    heapq.heappush(done, a + d)
                else:  # 대기시간이 발생하는 경우
                    w = x - a
                    t += w  # 대기시간 추가
                    heapq.heappush(done, x + d)
                # print(done)
            time[i].append(t)

            # m == 0인 경우를 제외하고는 가능한 조합 구해서 최솟값 찾기

    all_combis = itertools.product(range(m + 1), repeat=k)
    valid_combis = [comb for comb in all_combis if sum(comb) == m]

    # print(valid_combis)
    answer = 2e9
    for comb in valid_combis:
        temp = 0
        # print("comb ", comb[0])
        for i in range(k):
            temp += time[i + 1][comb[i]]
        answer = min(answer, temp)
        # print(time)
    return answer