# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Diameter is left height + right height + 1 right
# The thing is we gotta keep track of the max

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # return height
        def dfs(curr):
            if not curr:
                return 0

            lh = dfs(curr.left)
            rh = dfs(curr.right)

            self.res = max(self.res, lh + rh)
            return 1 + max(lh, rh)
        
        dfs(root)
        return self.res