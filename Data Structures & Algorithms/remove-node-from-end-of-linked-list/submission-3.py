# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # The non memory efficient solution would be to use a stack
        # Then we can easily locate which node this question is talking about

        # The other way is to iterate throught the node one time, while we have two pointers
        # That have n space between them, that way, when the right pointer reaches null we can be sure the l pointer would point to the n node
        # 1 2 3 4
        # l1 2 r3 4
        # 1 l2 3 r4
        # 1 2 l3 4 r
        # 1 2 4

        # Or to be efficient we can check for r.next instead, if its null we just delete the next of l
        # lets see for weird cases
        # 5.l None.r 
        # Oh so another rule, if r is actually none, we should just delete l?
        # 1l 2 None.r

        # 1l 2r

        # First we gotta define left and right
        left = right = head

        for i in range(n):
            right = right.next

        # Now we should iterate them, one by one until r meets criteria
        while right and right.next:
            left = left.next
            right = right.next
        
        # this right is none, so we delete l and move on
        if not right:
            if left.next:
                head = left.next
            else:
                head = None
        else:
            left.next = left.next.next
    
        return head


