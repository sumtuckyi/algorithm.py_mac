# 이진트리의 서브패스로서 연결리스트와 일치하는 부분 찾기 - dfs로 트리 탐색하기 1367
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        answer = [False]

        def dfs(root_node):
            if root_node is None:
                return

            find_subpath(root_node, head)
            if root_node.left:
                dfs(root_node.left)
            if root_node.right:
                dfs(root_node.right)

        def find_subpath(tree_node, head_node):
            if tree_node.val == head_node.val:  # 일치하는 경우
                if head_node.next is None:  # 경로를 찾은 경우
                    answer[0] = True
                    return
                    # 다음 노드도 일치하는지 왼쪽 아래로 탐색
                if tree_node.left:
                    find_subpath(tree_node.left, head_node.next)
                if tree_node.right:  # 오른쪽 아래로 탐색
                    find_subpath(tree_node.right, head_node.next)

        dfs(root)

        return answer[0]

