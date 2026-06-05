# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head
        
        while curr:
            next_pointer = curr.next # None

            curr.next = prev # 3->2

            prev = curr # 3
            curr = next_pointer # None
      
        return prev


        