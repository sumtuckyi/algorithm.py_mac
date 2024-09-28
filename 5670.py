import sys
input = sys.stdin.readline
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def count_input(self, word):
        node = self.root
        count = 0
        for char in word:
            if node == self.root:
                count += 1
            else:
                if len(node.children) != 1 or node.is_end:
                    count += 1
            node = node.children[char]
        return count


while 1:
    try:
        N = int(input())

        words = []
        for _ in range(N):
            words.append(input().rstrip())

        trie = Trie()
        for word in words:
            trie.insert(word)

        res = 0
        for word in words:
            res += trie.count_input(word)
        ans = (res / N)
        print(f'{ans:.2f}')
    except:
        break
