# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        #Approach: Recursive DFS
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, n and h are the size and height of the tree, respectively
        
        self.result = 0
        self.helper(root)
        return self.result
    
    def helper(self, root):
        #base
        if not root:
            return 0
        
        #logic
        extraCoins = self.helper(root.left) + self.helper(root.right) + root.val - 1
        self.result += abs(extraCoins)
        return extraCoins
