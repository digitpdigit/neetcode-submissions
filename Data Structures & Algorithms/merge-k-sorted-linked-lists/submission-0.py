# Assumptions:
# - all array is sorted, both the big array and small array

# Naive: We can traverse everything
# take the first element of each array and then compare
# O(n*k) k = sum length of all list

# Strategy
# We can merge the array two by two?
# Something like merge(lists[0], lists[1])
# index = 1 and result will be put in lists 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, first: ListNode, second: Optional[ListNode]):
        if not second:
            return first

        head = ListNode()
        curr = head

        while first and second:
            if first.val > second.val:
                curr.next = second
                second = second.next
            else:
                curr.next = first
                first = first.next
            
            curr = curr.next
        
        if first:
            curr.next = first
        if second:
            curr.next = second
        
        return head.next

    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
            
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])
        
        return lists[len(lists)-1]
        