# lca찾기(단일 쿼리) - 2096
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """

        # 두 노드의 LCA를 찾는 함수
        def find_lca(root, s, t):  # root가 탐색의 시작점
            if root is None or root.val == s or root.val == t:
                return root

            left = find_lca(root.left, s, t)
            right = find_lca(root.right, s, t)

            if left and right:
                return root
            elif left:
                return left
            else:
                return right

        def find_path(node, target, path):  # node에서 target까지의 경로 찾기
            if node is None:  # 더 이상 자식 노드가 없으면
                return False
            if node.val == target:  # 목표 노드에 도달하면 리턴
                return True

            # 그렇지 않다면 계속 재귀적으로 트리 하부로 탐색
            # 왼쪽 노드를 먼저 탐색하는 이유가 있음 - 트리가 불균형
            if node.left and find_path(node.left, target, path):  # 왼쪽 자식 노드가 존재하고 마지막 재귀 호출에서 목표 노드를 찾아서 거술러 올라오면서 왼쪽인 경로를 저장
                path.append('L')  # 왼쪽 자식노드에서 거슬러 올라가면서 경로를 저장
            elif node.right and find_path(node.right, target, path):  # 마찬가지로 오른쪽인 경로를 저장
                path.append('R')
            return len(path) > 0

        lca = find_lca(root, startValue, destValue)
        # print(lca)
        from_lca_to_s = []
        find_path(lca, startValue, from_lca_to_s)
        from_lca_to_s = ''.join(['U' for _ in range(len(from_lca_to_s))])  # 시작점에서 lca까지의 경로는 모두 U

        from_lca_to_t = []  # t에서 lca까지의 순서로 경로가 기록됨
        find_path(lca, destValue, from_lca_to_t)
        from_lca_to_t = ''.join(reversed(from_lca_to_t))  # 따라서 경로를 뒤집어야 lca -> t

        return from_lca_to_s + from_lca_to_t
