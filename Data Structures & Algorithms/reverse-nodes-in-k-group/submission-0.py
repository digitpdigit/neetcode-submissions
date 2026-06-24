# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We can do first iteration to split the list into two, based on k
# We reverse separately then merge all together...
# it will take O 2n since we basically iterate the list two times
# lets see if we can iterate once
# But theres a requirements to keep the node as is if the length < k, that means we gotta know wether to reverse it or not first
# So first thorough iteration should be essential
# We can have a function that reverse a group, then return the head and tail
# Therefore recursively we can assign next of current tail to the next head?


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if length exceeds k
        checker = head
        tempK = k
        while checker and tempK > 1:
            checker = checker.next
            tempK -= 1
        
        if not checker or tempK > 1:
            return head
       

        tail = None
        prev = None
        temp = None

        tempK = k
        while head and tempK > 0:
            temp = head.next
            head.next = prev

            if not prev:
                tail = head

            prev = head
            head = temp
            tempK -= 1
        
        tail.next = self.reverseKGroup(temp, k)
        
        return prev





        