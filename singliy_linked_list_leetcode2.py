# 단일 연결 리스트에 새로운 노드 삽입하기 - 2807
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        left = head
        right = head.next

        while True:
            if right is None:
                return head

            new_val = math.gcd(left.val, right.val)
            new_node = ListNode(new_val)
            left.next = new_node
            new_node.next = right
            left = right
            right = left.next
