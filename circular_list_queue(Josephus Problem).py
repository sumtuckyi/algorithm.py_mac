from collections import deque


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 1

        q = [i for i in range(1, n + 1)]

        idx = 0  # 시작점
        while len(q) > 1:
            # k만큼 이동
            target_idx = (idx + k - 1) % len(q)
            q.pop(target_idx)  # 탈락자 발생
            idx = target_idx  # 탈락자 자리를 다음 사람이 채운다고 생각
        return q[0]


class Solution2(object):

    def find_the_winner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 1

        q = deque([i for i in range(1, n + 1)])

        idx = 0  # 시작점
        while len(q) > 1:
            # k만큼 이동
            for _ in range(k - 1):
                q.append(q.popleft())  # 가장 왼쪽의 요소를 k-1회 만큼 순서대로 오른쪽으로 옮긴다.
            q.popleft()  # 탈락자 발생
        return q[0]





