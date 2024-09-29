# 이중 연결 리스트 - 432
# 해시테이블 만으로는 최대, 최소 등장 빈도에 해당하는 단어를 O(1)로 찾을 수 없으므로
# 연결 리스트를 활용한다.

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}  # 맵을 이용해 키가 담긴 노드로 이동한다.

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq  # 현재 빈도를 저장
            node.keys.remove(key)

            next_node = node.next  # 현재 빈도 노드의 바로 다음 노드
            if next_node == self.tail or next_node.freq != freq + 1:
                # 새 노드를 만든다.
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                new_node.prev = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                self.map[key] = new_node
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

            if not node.keys:  # 키가 이동하므로써 이전 노드가 비어버린 경우에는 삭제
                self.remove_node(node)
        else:  # 키가 없다면
            first_node = self.head.next
            if first_node == self.tail or first_node.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.prev = self.head
                new_node.next = first_node
                self.head.next = new_node
                first_node.prev = new_node
                self.map[key] = new_node
            else:  # 빈도가 1인 노드가 있다면
                first_node.keys.add(key)
                self.map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]  # key가 담겨 있는 노드를 찾기
        node.keys.remove(key)
        freq = node.freq  # 기존 빈도를 저장

        if freq == 1:  # 이번 함수 호출로 빈도가 0이 되는 경우
            del self.map[key]  # map에서 key를 아예 삭제
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                # 새 노드 만들고 빈도는 freq - 1로 할당하기
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.map[key] = new_node
            else:  # freq - 1 인 노드가 존재할 때
                prev_node.keys.add(key)
                self.map[key] = prev_node

        if not node.keys:
            self.remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(
            iter(self.tail.prev.keys)
        )  # 테일 노드의 바로 앞에 있는 노드의 키 중 하나를 리턴

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(
            iter(self.head.next.keys)
        )

    def remove_node(self, node):  # freq가 0이 된 노드를 삭제
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()