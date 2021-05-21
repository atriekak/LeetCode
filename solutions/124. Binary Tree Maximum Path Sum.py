# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #Approach: Recursion // Post-order Traversal
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, n is the height of the tree, and h is the size of the tree
        
        self.result = - inf
        self.helper(root)
        return self.result
    
    def helper(self, root):
        #base
        if not root:
            return 0
        
        #logic
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.result = max(self.result, root.val + max(left, 0) + max(right, 0))
        
        return root.val + max(left, right, 0)
