# 주어진 전화번호를 트라이에 삽입한다.
# 삽입 시에 어떤 한 번호가 다른 번호의 접두어가 되는 경우, 중단한다.
# 겹치지 않을 경우 계속해서 삽입한다.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for idx, digit in enumerate(number):
            if digit in node.children:
                node = node.children[digit] # 이동
                if node.is_end or idx == len(number) - 1:  # 이동했는데 해당 노드가 어떤 번호의 끝이면
                    return False
            else:
                node.children[digit] = TrieNode()
                node = node.children[digit]
        node.is_end = True
        return True


T = int(input())

for _ in range(T):
    N = int(input())
    trie = Trie()
    numbers = []
    for _ in range(N):
        numbers.append(input())

    tof = False
    for num in numbers:
        if not trie.insert(num):
           tof = True
           break

    if tof:
        print('NO')
        continue
    else:
        print('YES')


