# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We can traverse down each of our leaves, recursively
# A parent maxDepth should be max of maxDepth of left and right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        md_left, md_right = 0, 0
        if root.left:
            md_left = self.maxDepth(root.left)
        if root.right:
            md_right = self.maxDepth(root.right)

        md = max(md_left, md_right)

        return md + 1

        
        