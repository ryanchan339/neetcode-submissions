# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def find(curr):
            if val < curr.val:
                if not curr.left:
                    return curr
                return find(curr.left)
            elif val > curr.val:
                if not curr.right:
                    return curr
                return find(curr.right)
        
        parent = find(root)
        if val < parent.val:
            parent.left = TreeNode(val)
        elif val > parent.val:
            parent.right = TreeNode(val)


        return root