# 이진 트리를 postorder 순회하기 - 재귀 대신 반복문 사용하기 - 145문
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        stack1 = []
        stack2 = []
        stack1.append(root)

        while stack1:
            node = stack1.pop()
            stack2.append(node.val)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        return stack2[::-1]