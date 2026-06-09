"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # The brute force solution would be to iterate twice and save the index of each node
        copied = Node(0, None, None)
        temp2 = copied
        record = {}
        temp = head

        while temp:
            temp2.val = temp.val
            if temp.next:
                temp2.next = Node(0, None, None)

            if not temp.random:
                temp2.random = None

            record[temp] = temp2

            temp = temp.next
            temp2 = temp2.next

        
        # Now we have record of which node each index is
        temp = head
        temp2 = copied

        while temp:
            if temp.random:
                temp2.random = record[temp.random]

            temp = temp.next
            temp2 = temp2.next
    

        return copied