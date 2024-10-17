# 문자열의 길이는 최대 60만까지 늘어날 수 있음
# 쿼리의 수는 최대 50만..
# 10만 단위의 배열을 탐색하고 조작하려면..? 스택이나 투 포인터 사용이 효율적..

# 4가지 명령어를 구현해야함
# 이중 연결 리스트 사용
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, s):  # 초기문자열 s로 초기화
        self.head = Node(0)
        self.tail = Node(0)
        self.cursor = self.tail  # 처음에 커서는 문장의 맨 뒤에 위치
        self.head.next = self.tail
        self.tail.prev = self.head

        first_node = self.head
        for i in range(len(s)):  # 이중 연결 리스트 만들기
            new_node = Node(s[i])  # 추가할 노드
            first_node.next = new_node
            new_node.prev = first_node
            new_node.next = self.tail
            self.tail.prev = new_node
            first_node = new_node

    def delete_char(self):  # 쿼리가 B일 때 호출
        # 커서가 문장의 맨 앞이면 무시한다.
        if self.cursor.prev == self.head:
            return
        cur_node = self.cursor  # 커서 위치를 기준으로
        target_node = cur_node.prev  # 삭제할 노드
        tar_prev = target_node.prev
        cur_node.prev = tar_prev
        tar_prev.next = cur_node
        # 커서 위치는 그대로

    def insert_char(self, char):  # 쿼리가 P일 때 호출, char 노드를 커서 왼쪽에 추가
        new_node = Node(char)  # 추가할 노드
        cur_node = self.cursor  # 커서 위치를 기준으로
        prev_node = cur_node.prev  # 새 노드의 이전 노드가 될 노드
        new_node.prev = prev_node
        new_node.next = cur_node
        prev_node.next = new_node
        cur_node.prev = new_node

    def move_right(self):  # 커서를 오른쪽으로 이동
        # 커서가 문장의 맨 뒤면 무시
        if self.cursor == self.tail:
            return
        next_node = self.cursor.next
        self.cursor = next_node

    def move_left(self):  # 커서를 왼쪽으로 이동
        # 커서가 문장의 맨 앞이면 무시
        if self.cursor.prev == self.head:
            return
        prev_node = self.cursor.prev
        self.cursor = prev_node


s = input()
string = DLL(s[:-1])
N = int(input())  # 쿼리의 개수
for _ in range(N):
    line = list(input().split())
    if len(line) == 2:  # 문자를 추가하는 쿼리의 경우
        string.insert_char(line[1])
    else:
        if line[0] == 'L':
            string.move_left()
        elif line[0] == 'D':
            string.move_right()
        else:  # 삭제
            string.delete_char()

# 남은 연결리스트 노드의 값을 모두 출력
# head 다음 노드부터 출력
ans = []
string.cursor = string.head
while string.cursor.next != string.tail:  # 꼬리 노드에 도착할 때까지
    next_node = string.cursor.next
    ans.append(next_node.value)
    string.cursor = next_node
    # print(ans)
print(''.join(ans))