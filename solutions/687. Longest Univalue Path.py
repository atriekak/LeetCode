# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        #Approach: Recursion
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        
        self.result = 0
        self.helper(root)
        return self.result
    
    def helper(self, root):
        #base
        if not root:
            return 0
        
        #logic
        left = self.helper(root.left) + 1
        if not root.left or root.left.val != root.val:     #no same value path on left
            left = 0
        
        right = self.helper(root.right) + 1
        if not root.right or root.right.val != root.val:   #no same value path on right
            right = 0
        
        self.result = max(self.result, left + right)
        return max(left, right)
