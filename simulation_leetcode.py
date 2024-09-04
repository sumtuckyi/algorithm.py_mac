# 시뮬레이션 - 장애물 위치 확인시 딕셔너리(해시테이블) 이용 - 874
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        ob_dict = defaultdict(list)
        for x, y in obstacles:
            ob_dict[x].append(y)

        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0  # 처음에는 북쪽을 향함 - % 4하여 이용, 북동남서 = 0123
        cur = [0, 0]  # 시작점 초기화, 현재 위치로 갱신
        max_dist = [0]

        def move_forward(k):  # k만큼 dir 방향으로 이동하되, 장애물을 만나면 종료
            for _ in range(k):  # k번 반복
                dx, dy = delta[dir % 4]
                # 현재 로봇이 향한 방향으로 k칸 만큼 이동하고 현재 위치를 갱신
                # 이동할 위치에 장애물이 있는지 확인
                nxt_x, nxt_y = cur[0] + dx, cur[1] + dy
                if nxt_y in ob_dict[nxt_x]:  # 장애물이 있다면 현재 칸에서 정지한 다음 리턴
                    return
                cur[0], cur[1] = nxt_x, nxt_y
                max_dist[0] = max(max_dist[0], cur[0] ** 2 + cur[1] ** 2)  # 갈수있는 최대 거리 갱신

        # 명령어 처리
        for com in commands:
            if com == -1:  # 오른쪽으로 90도 회전
                dir += 1
            elif com == -2:  # 왼쪽으로 90도 회전
                dir -= 1
            else:
                move_forward(com)  # 앞으로 k칸 이동

        # print(cur, max_dist)
        return max_dist[0]