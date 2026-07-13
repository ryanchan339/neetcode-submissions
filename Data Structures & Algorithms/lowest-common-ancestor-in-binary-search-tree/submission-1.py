# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        def dfs(node):
            nonlocal res
            if not node:
                return ""
            #print(node.val)
            if node.val == p.val:
                if dfs(node.left) == 'q' or dfs(node.right) == 'q':
                    res = node 
                return 'p'
            if node.val == q.val:
                if dfs(node.left) == 'p' or dfs(node.right) == 'p':
                    res = node 
                return 'q'
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                res = node
                return ""
            if left == 'p' or left == 'q':
                return left
           
            if right == 'p' or right == 'q':
                return right
            return ""
        dfs(root)
        return res