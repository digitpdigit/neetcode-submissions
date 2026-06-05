# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Lets do it recursively
        # To do something recursively we need to think of subproblem
        # 0 1 2 3
        # we gotta reverse 1 2 3 meaning reverse 2 3 and so on
        # But we stop at 2 3, because 3 None is irreversable

        # This is the boundaries as to stop the recursion
        if head == None or head.next == None:
            return head
        
        # We reverse the rest of the list but this one
        result = self.reverseList(head.next)

        # The main function will look something like
        head.next.next = head
        head.next = None

        # This will look something like
        # 0 -> 1 -> 2 -> 3
        # 0 -> 1 -> 2 <- 3 , 2 -> None
        # 0 -> 1 <- 2 <- 3 , 1 -> None
        # None <- 0 <- 1 <- 2 <- 3 

        return result 


        


        