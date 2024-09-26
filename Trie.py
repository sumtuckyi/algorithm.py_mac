class TrieNode:
    def __init__(self):
        self.children = {}  # 자식노드를 담을 딕셔너리
        self.is_end = False  # 어떤 단어의 끝나는 문자인지


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str): # word를 트리에 삽입하기
        node = self.root
        for char in word:
            # 현재 문자가 node의 자식 노드에 없으면 새 노드를 추가
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # 추가한 노드로 이동
        node.is_end = True # 마지막 문자까지 추가햐고 그 문자를 담은 노드의 속성 값 변경


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 현재 문자가 node의 자식 노드에 없으면 트리에 단어가 존재하지 않는 것임
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end # word를 접두사로 가지는 단어는 있으나, 완전히 일치하는 단어는 없는 경우라면 False를 반환


    def starts_with(self, prefix : str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True # 반복문을 끝까지 돌면 해당 접두사가 존재하는 것이므로 True를 반환

