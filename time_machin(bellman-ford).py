from copy import deepcopy


def BF(start):
    global tof
    # N-1번 반복
    for k in range(N):
        # 모든 정점에 대해
        for i in range(1, N + 1):
            #모든 간선을 확인
            for j in range(len(adj_li[i])):
                # 간선의 시작점이 도착지로서 한 번도 계산된 적이 없다면 패스
                if distance[i] == float('inf'):
                    continue
                # 기존 최단거리와 새로운 경로의 걸리는 시간을 비교하여 갱신
                if distance[i] + adj_li[i][j][1] < distance[adj_li[i][j][0]]:
                    distance[adj_li[i][j][0]] = distance[i] + adj_li[i][j][1]
                    if k == N-1:
                        tof = True


N, M = map(int, input().split())
#N번 도시까지의 최단거리
distance = [0, 0] + [float('inf') for _ in range(N-1)]
#간선정보는 인접리스트로 저장
adj_li = [[] for _ in range(N + 1)]
#인접리스트 채우기
for i in range(M):
    f, t, time = map(int, input().split())
    adj_li[f].append([t, time])

tof = False
BF(1)

# 음수간선 순환이 존재하면 -1만 출력
if tof:
    print(-1)
    exit()
# 해당 도시까지의 경로가 존재하지 않는다면 해당 도시의 순서에서 -1을 출력
for i in range(2, N + 1):
    if distance[i] == float('inf'):
        distance[i] = -1

print(*distance[2:], sep='\n')
