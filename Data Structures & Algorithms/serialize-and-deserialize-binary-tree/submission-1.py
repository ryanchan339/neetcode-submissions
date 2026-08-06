# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = 'N'
#         self.right = 'N'

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            curr = queue.popleft()
            if not curr or curr == 'N':
                res.append('N')
                continue
            res.append(str(curr.val))
            if curr.left != 'N':
                queue.append(curr.left)
            else:
                queue.append('N')
            if curr.right != 'N':
                queue.append(curr.right)
            else:
                queue.append('N')    
        return ",".join(res)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #2 5
        #1 2 3 N N 4 5
        if not data or data[0] == 'N':
            return None
        data = data.split(',')
        queue = deque()
        i = 1
        root = TreeNode(data[0])
        queue.append(root)
        while queue:
            
            curr = queue.popleft()
            if not curr or curr == 'N':  
                continue
            if i < len(data):
                if data[i] == 'N':
                    curr.left = None
                else:
                    curr.left = TreeNode(data[i])
                    queue.append(curr.left)
            i += 1
            if i < len(data):
                if data[i] == 'N':
                    curr.right = None
                else:
                    curr.right = TreeNode(data[i]) 
                    queue.append(curr.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))