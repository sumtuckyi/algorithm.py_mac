# 루트에서부터 dfs 탐색하여 리프노드간의 거리 구하기 - 1530
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """

        self.cnt = 0

        def dfs(node):
            if not node:
                return []

            # 리프노드라면
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:  # left는 node 기준으로 왼쪽 서브트리에 속한 리프 노드까지의 거리
                for r in right:
                    if l + r <= distance:
                        self.cnt += 1

            return [d + 1 for d in left + right if d + 1 < distance]

        dfs(root)
        return self.cnt




