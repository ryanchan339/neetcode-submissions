# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = []
        res = 0
        def dfs(node):
            nonlocal stack
            nonlocal res
            if not node:
                return
            if stack and stack[-1] > node.val:
                dfs(node.left)
                dfs(node.right)
            else:
                res += 1
                stack.append(node.val)
                dfs(node.left)
                dfs(node.right)
            if stack and node.val == stack[-1]:
                stack.pop()
            
        dfs(root)
        
        return res