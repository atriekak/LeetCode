# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
from collections import deque
​
class Codec:
    #Approach: BFS
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    #where, n is the size of the tree
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        sb = []
        de = deque([root])
        
        while de:
            root = de.popleft()
            if root:
                sb.append(str(root.val))
                
                de.append(root.left)
                de.append(root.right)
            
            else:
                sb.append('None')
                
        return ','.join(sb)
​
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        data = data.split(',')
        head = TreeNode(data[0])
        
        de = deque([head])
        
