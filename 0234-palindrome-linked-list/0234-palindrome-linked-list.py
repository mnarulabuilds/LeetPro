# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True

        slow, fast = head, head
        half_stack = []

        # 1,2,2,1
        # 1,3,4,3,1

        while fast:
            half_stack.append(slow.val)
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        while slow:
            curr_val = half_stack.pop() if len(half_stack) else None
            if curr_val != slow.val:
                return False
            slow = slow.next

        return True 
