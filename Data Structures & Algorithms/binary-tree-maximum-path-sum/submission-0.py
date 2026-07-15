# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def maxPath(node):
            nonlocal res
            if not node:
                return 0
            left = maxPath(node.left)
            right = maxPath(node.right)
            res = max(res, left + node.val, right + node.val, left + right + node.val, node.val)
            curr = max(left + node.val, right + node.val, node.val)
            return curr

        maxPath(root)
        return res