def bellman_ford(start, n, edges):
    # 초기 거리 배열: 무한대로 초기화
    distance = [float('inf')] * n
    distance[start] = 0  # 시작 노드의 거리는 0

    # 모든 간선에 대해 V-1번 반복 : 그래프에 V개의 노드가 있으면, 최단 경로는 최대 V-1개의 간선을 포함할 수 있기 때문
    for i in range(n - 1):
        for s, e, w in edges: # 모든 간선에 대해
            if distance[s] != float('inf') and distance[s] + w < distance[e]:
                distance[e] = distance[s] + w # 도착노드까지의 최단 거리 갱신

    # 음수 사이클 확인 : 모든 간선에 대해 한 번 더 최단 거리 갱신
    for s, e, w in edges:
        if distance[s] != float('inf') and distance[s] + w < distance[e]: # 이때 갱신되면 음수 사이클이 존재하는 것이다.
            print("음수 사이클이 존재합니다.")
            return None  # 음수 사이클이 있으면 경로를 정의할 수 없음

    return distance  # 최단 거리 배열 반환
