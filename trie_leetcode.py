# 단어의 중복이 존재 + 접두사가 사용된 단어의 수 합산 방식이 어려운 문제 - 2416
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word_count = 0  # 같은 단어가 몇 개 존재하는지 기록
        self.prefix_count = 0  # 해당 노드가 접두사의 마지막 문자열인 경우, 해당 접두사가 몇 개의 단어에서 등장하는지 카운트


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.dict = defaultdict(int)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end = True
        node.word_count += 1  # 트라이에 새 문자열을 삽입할 때, 접두사의 등장횟수를 기록

    def count_prefix(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            score += node.prefix_count
        return score

    # def count_words(self, node: TrieNode, prefix: str) -> None:
    #     if node.is_end:
    #         self.dict[prefix] += node.word_count # 단어 등장 횟수 만큼 단어의 수를 카운트
    #     for char, child in node.children.items():
    #         self.count_words(child, prefix)

    # def count(self, prefix: str) -> None:
    #     node = self.root
    #     for char in prefix:
    #         if char not in node.children:
    #             return False
    #         node = node.children[char]
    #     # 단어를 찾음
    #     self.count_words(node, prefix)


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # 트라이 인스턴스 생성
        trie = Trie()

        # 트라이에 단어 삽입
        for word in words:
            trie.insert(word)

        res = []
        # 트라이에서 접두사의 등장 횟수 세기 - 이미 등장한 접두사면 패스
        for word in words:
            res.append(trie.count_prefix(word))

        # print(trie.dict)
        return res
