# TreeNode 클래스를 이용하여 이진 트리 생성하기 - 2196
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """

        node_map = {}  # key는 노드의 value이고 value는 Treenode 인스턴스
        children = set()

        for node in descriptions:
            par = node[0]
            child = node[1]
            is_left = bool(node[2])

            if par not in node_map:
                node_map[par] = TreeNode(par)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if is_left:
                node_map[par].left = node_map[child]  # 왼쪽 자식의 형태는 마찬가지로 Treenode
            else:
                node_map[par].right = node_map[child]

            children.add(child)  # tree의 루트 노드를 찾기 위해 자식 노드의 값만 저장

        for node in node_map.values():  # Treenode인스턴스만 탐색
            if node.val not in children:
                return node  # 루트 노드 반환