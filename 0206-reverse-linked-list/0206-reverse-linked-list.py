# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        oldHead = head
        tail = head.next
        newHead = self.reverseList(tail)
        head.next = None
        tail.next = oldHead

        return newHead

        