# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        ans, one , two = None, list1, list2
        if one.val < two.val:
            ans = one
            one = one.next
        else:
            ans = two
            two = two.next

        sorted_list = ans

        while one and two:
            if one.val < two.val:
                sorted_list.next = one
                one = one.next
            else:
                sorted_list.next = two
                two = two.next
            sorted_list = sorted_list.next

        while one:
            sorted_list.next = one
            one = one.next
            sorted_list = sorted_list.next

        while two:
            sorted_list.next = two
            two = two.next 
            sorted_list = sorted_list.next
        
        return ans