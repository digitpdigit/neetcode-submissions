# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0, n-1, 1, n-2
        # first, last, second, last-1, third, last-2
        # Two pointer first and last
        # First point to last, last point to second, second point to second last, and so on
        # l -> r -> l -> r -> l -> r
        
        # Iterations
        # .0 1 2 3 4 5 6.
        # 0 6 1 2 3 4 5 6
        # 0 6 1 5 2 3 4 5 6

        # Can i modify the listNode to have prev value?
        #  if yes, we can iterate once and add prev to all those node, then we reiterate with two pointers
        #  if no, i can iterate once to put all into stack, and we can do pop and popleft to do reordering

        stack = collections.deque()
        temp = head
                
        while temp:
            stack.append(temp)
            temp = temp.next

        # Now we have the stack with exact same order as the head
        # We can start to iterate
        # popleft -> smallest -> first thing, will point to...
        # pop

        # Iterations
        # deque([2, 4, 6, 8])
        # 2 -> 8 -> 4 -> 6
        # if we at the end of the stack we point to None
        # Lets first remove the bottom
        stack.popleft()
        temp = head
        index = 1
                
        while len(stack) > 0:
            # if even
            if index % 2 == 0:
                temp.next = stack.popleft()
            else:
                temp.next = stack.pop()
            
            index+=1
            temp = temp.next
        
        temp.next = None
        
        return None


        