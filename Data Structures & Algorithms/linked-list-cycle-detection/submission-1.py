# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Lets assume all node has different value, that way when we encounter the same value we can say that this list is cyclic
        record = set()

        while head:
            if head in record:
                return True
            else:
                record.add(head)
            
            head = head.next
        
        return False
        