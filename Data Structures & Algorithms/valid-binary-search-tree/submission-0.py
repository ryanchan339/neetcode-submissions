# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        def inOrder(node):
            nonlocal order
            if not node:
                return
            inOrder(node.left)
            order.append(node.val)
            inOrder(node.right)
        inOrder(root)
        set1 = set()
        for n in order:
            if n in set1:
                return False
            set1.add(n)
        return order == sorted(order)