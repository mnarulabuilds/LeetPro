# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        curr = head

        while curr and curr.val == val:
            curr = curr.next

        head = curr

        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            if curr:
                curr = curr.next
    
        return head
