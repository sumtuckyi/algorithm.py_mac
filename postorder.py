N, K = map(int, input().split())
V = int(input())
adj_m = [[0] * (N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(K):
    x, y = map(int, input().split())
    adj_m[x][y] = 1

def preorder(v): # v에서 전위순회 시작
    visited[v] = 1
    print(v, end = ' ')
    for i in range(N, 0, -1):
        if adj_m[v][i] == 1 and not visited[i]:
            preorder(i)


visited2 = [0]*(N+1)

# 오른쪽(즉, 더 큰 쪽 노드 먼저)-> 왼쪽 -> 루트
def postorder(v):
    for i in range(N, 0, -1):  # 큰 번호 우선
        #print(f'{i}번째 인접노드')
        if adj_m[v][i] == 1 and not visited2[i]: # 하위 노드가 있고 아직 방문하지 않았다면
            postorder(i)
            continue
    print(v, end=' ')
    visited2[v] = 1
    return

preorder(V)
print()
postorder(V)


'''
6 5
1
1 2
1 4
2 3
4 5
4 6

5 6
1
1 3
1 4
4 2
4 3
4 5
3 5
'''