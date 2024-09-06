# 싱글 연결 리스트 - 탐색하면서 특정 노드만 삭제하기
# in 연산 : list를 사용하면 시간복잡도가 O(len(list)), set를 사용하면 O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        num_set = set(nums)
        cur_node = head
        before = None

        while cur_node is not None:
            # 첫번째 노드부터 탐색
            if cur_node.val in num_set:  # 삭제 대상이라면
                # 맨 앞의 노드라면 - 바로 삭제하면 됨
                if before is None:
                    head = cur_node.next
                    # 다음 노드를 탐색
                    cur_node = head
                else:  # 이전 노드가 있는 경우라면
                    before.next = cur_node.next
                    # 다음 노드를 탐색
                    cur_node = cur_node.next
            else:  # 삭제 대상이 아닌 경우
                before = cur_node
                cur_node = before.next

        return head
