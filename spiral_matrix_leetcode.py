# 2차원 배열을 나선 순회하기 - 2326
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        grid = [[-1 for _ in range(n)] for _ in range(m)]

        d = 0  # 향하는 방향(오른쪽-0, 아래쪽-1, 왼쪽-2, 위-3)
        # 탐색방향 조정 - 이전 방향과 동일하게 가되 만약 그리드의 범위를 벗어나거나 이미 방문했다면 다음 방향으로 전환
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        idx = 1
        current = head
        grid[0][0] = current.val
        current = current.next  # 이 값이 None일수도
        cur_x, cur_y = 0, 0
        next_x, next_y = cur_x + delta[d % 4][0], cur_y + delta[d % 4][1]
        while idx < m * n:  # 총 m * n 칸을 채운다.
            # print('여기로 이동', next_x, next_y)
            # 다음 칸 좌표 검사
            if (0 <= next_x < m and 0 <= next_y < n) and grid[next_x][next_y] == -1:  # 범위 안이면서 빈칸이면
                # 연결리스트 현재 노드 값이 존재하면
                if current:
                    # print('노드 값', current.val)
                    # print('좌표', next_x, next_y)
                    grid[next_x][next_y] = current.val
                    current = current.next  # 연결리스트 포인터 이동
                    # print(grid)
                else:  # 연결리스트가 끝났으면
                    break
                    # grid[next_x][next_y] = -1
                idx += 1
                cur_x, cur_y = next_x, next_y  # 현재 좌표 갱신
                next_x, next_y = cur_x + delta[d % 4][0], cur_y + delta[d % 4][1]

            else:  # 범위 안이 아니거나 빈칸이 아니면
                d += 1  # 방향 전환
                next_x, next_y = cur_x + delta[d % 4][0], cur_y + delta[d % 4][1]
                # print(d, '방향 전환', '새 좌표', next_x, next_y)

        return grid



