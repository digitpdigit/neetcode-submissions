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

        newlist = None
        curr = None

        while list1 or list2:
            # print(list1)
            l1 = list1
            l2 = list2 
            
            # if l1 smaller then we put l1 as the new node in newlist
            if not l1:
                if not newlist:
                    newlist = l2
                    curr = newlist
                else:
                    curr.next = l2
                    curr = curr.next
                list2 = list2.next
            
            elif not l2:
                if not newlist:
                    newlist = l1
                    curr = newlist
                else:
                    curr.next = l1
                    curr = curr.next
                list1 = list1.next

            elif l1.val <= l2.val:
                if not newlist:
                    newlist = l1
                    curr = newlist
                else:
                    curr.next = l1
                    curr = curr.next
                list1 = list1.next
            else:
                if not newlist:
                    newlist = l2
                    curr = newlist
                else:
                    curr.next = l2
                    curr = curr.next
                list2 = list2.next
            
        
        return newlist




