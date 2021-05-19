# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        #Approach: Post-Order Traversal (Recursive DFS) // Greedy
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, n is the size of the tree, and h is the height of the tree
        
        self.count = 0
        if not root:
            return self.count
        
        self.helper(root)
        if root.val == 0:
            self.count += 1
        
        return self.count
    
    def helper(self, root):
        #base
        if not root:
            return
        
        #logic
        self.helper(root.left)
        self.helper(root.right)
        
        if (root.left and root.left.val == 2) or (root.right and root.right.val == 2):
            root.val = 1    # being monitored by one of child nodes
        if (root.left and root.left.val == 0) or (root.right and root.right.val == 0):
