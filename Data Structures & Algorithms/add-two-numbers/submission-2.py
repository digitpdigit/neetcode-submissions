# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        temp = result

        remainder = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            temp_sum = val1 + val2 + remainder

            # We sum, and if its more than 10 then we record the remainder for next calc
            if temp_sum >= 10:
                temp.val = temp_sum - 10 
                remainder = 1
            else:
                temp.val = temp_sum
                remainder = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # If theres still l1 or l2
            if l1 or l2 or remainder > 0:
                temp.next = ListNode(0, None)
            
            temp = temp.next
        
        if remainder > 0:
            temp.val = 1

        return result

