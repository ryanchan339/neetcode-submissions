# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def getHeight(node):
            if node == None:
                return -1
            return max(getHeight(node.left), getHeight(node.right)) + 1
        if abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return True
        
        
