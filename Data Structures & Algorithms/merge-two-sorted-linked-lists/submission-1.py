# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We can traverse both linked list at the same time and compare the value
        # if the value is smaller or same, we can set em to the next
        # The new list should be made up of nodes from list1 and list2.
        # So we create new list

        # Im thinking
        # 1 2 4
        # 1 3 5
        # 1 <= 1 -> 1
        # 2 4
        # 1 3 5
        # 1 <= 2 -> 1, 1
        # 2 4
        # 3 5
        # 2 <= 3 -> 1, 1, 2
        # 4 | 3 5
        # 3 <= 4 -> 1, 1, 2, 3
        # 4 | 5
        # 4 <= 5 -> 1, 1, 2, 3, 4
        # None | 5
        # 5 -> 1, 1, 2, 3, 4, 5

        newlist = ListNode()
        curr = newlist

        while list1 and list2:

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
            
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return newlist.next




