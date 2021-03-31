# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
from collections import deque
​
class Solution:
    #Solution 1
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #Approach: Iterative DFS w/ pruning -- pre-order
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        result = 0
        st = [root]
        
        while st:
            root = st.pop()
            if not root:
                continue
                
            if low <= root.val <= high:
                result += root.val
            if root.val > low:
                st.append(root.left)
            if root.val < high:
                st.append(root.right)
                
        return result
    
    #Solution 2
    """
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #Approach: Iterative DFS w/ pruning -- in-order
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        result = 0
        st = []
        while st or root:
            while root:
                st.append(root)
                if root.val > low:
                    root = root.left
                else:
                    break
            
            root = st.pop()
            if low <= root.val <= high:
                result += root.val
                
            if root.val < high:
