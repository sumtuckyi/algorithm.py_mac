# 노드 삭제 이후 트리 집합 구하기 - 1110
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        forest = []

        def find_node(root, is_root=True):
            # postorder - 왼쪽, 오른쪽, 부모 노드
            if root is None:
                return

            is_deleted = root.val in to_delete_set

            # 왼쪽 노드 탐색
            if root.left:
                root.left = find_node(root.left, is_deleted)

            # 오른쪽 노드 탐색
            if root.right:
                root.right = find_node(root.right, is_deleted)

            if is_deleted:  # 삭제할 노드라면
                # # 자식 노드 존재 시 분리된 트리를 forest에 저장
                # if root.left:
                #     print("append a new tree to forest", root.left)
                #     forest.append(root.left)
                # if root.right:
                #     print("append a new tree to forest", root.right)
                #     forest.append(root.right)
                return None

            if is_root:  # 어떤 트리의 루트이면서 삭제 대상이 아닌 경우
                forest.append(root)

            # 삭제할 노드가 아니라면
            return root

        find_node(root)
        return forest