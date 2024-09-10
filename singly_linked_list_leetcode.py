# 연결 리스트 절단하기 - 725
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # 연결리스트 노드 개수 구하기
        N = 0
        node = head
        res = []

        # 연결리스트가 비어있지 않은 경우, 노드의 개수 세기
        if node is not None:
            while True:
                N += 1
                node = node.next
                if node is None:
                    break

        # 그룹별 노드 개수 구하기
        part_size = N // k
        extra_nodes = N % k

        current = head
        for i in range(k):
            part_head = current  # 현재 파트의 시작점을 저장
            current_part_size = part_size + (1 if i < extra_nodes else 0)  # 앞에서부터 엑스트라 노드를 하나씩 추가한다.

            # 현재 파트의 마지막 노드까지 current가 이동
            for j in range(current_part_size - 1):  # 현재 부분의 길이만큼 이동한다.
                if current:
                    current = current.next

                    # Break the current part from the rest of the list
            if current:  # 충분히 이동했고 현재 파트의 마지막 노드에 도착했다면
                next_part = current.next  # 다음 파트의 시작노드 저장
                current.next = None  # 기존의 연결리스트 절단
                current = next_part  # 다음 파트의 시작점으로 이동

            # 절단된 현재 파트의 헤드를 반환 리스트에 추가
            res.append(part_head)

        return res

