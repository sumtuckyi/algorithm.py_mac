# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0  # 각 노드의 새로운 키 값이 될 누적합 초기화
        # reverse_inorder를 호출하여 TreeNode타입인 root의 값을 GST가 되도록 바꿔야한다.
        self.reverse_inorder(root)
        # print(root)
        return root

    def reverse_inorder(self, node):
        # 해당 노드의 오른쪽 자식 노드가 없다면
        if node is None:
            return
        self.reverse_inorder(node.right)
        self.total += node.val  # 누적합을 갱신
        node.val = self.total  # 해당 노드의 값도 누적합으로 갱신
        self.reverse_inorder(node.left)


