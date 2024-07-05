# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 투 포인터
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 두 개의 포인터 초기화
        modify = head.next  # 0이 아닌 첫 번째 노드
        next_sum = modify  # same

        while next_sum:
            sum = 0  # 블럭별 노드의 합
            # 블럭의 끝에 도달할 때까지
            while next_sum.val != 0:  # 도착한 노드의 값이 0이면 계산 중단
                sum += next_sum.val  # 노드의 값을 더하고
                next_sum = next_sum.next  # 다음 노드로 이동

            # 블럭의 시작 위치에 있는 modify의 값을 sum으로 변경
            modify.val = sum
            next_sum = next_sum.next  # 0이 아닌 다음 블럭의 노드로 이동 - 이 값이 None이면 다음 두 줄의 코드 실행 이후 반복문 종료
            modify.next = next_sum  # 기존 연결 리스트를 변경
            modify = modify.next  # next_sum과 같은 노드로 이동 - 마지막엔 None을 가리키게 됨

        return head.next

    # 재귀 함수
    def mergeNodes2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = head.next  # head가 다음 노드를 가리키게 함-인자로 받는 head는 시작이 0인 노드이기 때문
        if head is None:  # 마지막 노드에 도착하면
            return head  # 지금까지 만든 연결 리스트를 반환

        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            temp = temp.next

        # 0인 노드 - 기존 블럭의 끝이자 새로운 블럭의 시작 노드를 만난 경우
        head.val = sum
        head.next = self.mergeNodes(temp)
        return head

    # 새로운 연결 리스트 생성하여 반환
    def mergeNodes3(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 새로운 연결 리스트의 더미 헤드 생성
        dummy = ListNode(0)
        current = dummy

        # 합계를 저장할 변수
        sum = 0

        # 원본 리스트 순회
        node = head.next  # 첫 번째 0은 건너뛰기
        while node:
            if node.val == 0:
                # 0을 만나면 새 노드 생성 및 연결
                if sum > 0:
                    new_node = ListNode(sum)
                    current.next = new_node
                    current = current.next
                sum = 0  # 합계 초기화
            else:
                sum += node.val
            node = node.next

        return dummy.next
