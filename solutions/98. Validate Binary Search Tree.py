# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    #Solution 1
    def isValidBST(self, root: TreeNode) -> bool:
        #Approach: recursive; uses the min-max constraints over nodes in BST
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, h is the height of the BST
        
        return self.isValid(root, None, None)
    
    def isValid(self, root, minimum, maximum):
        #base
        if not root:
            return True
        
        #logic
        if minimum != None and root.val <= minimum:
            return False
        if maximum != None and root.val >= maximum:
            return False
        
        return (self.isValid(root.left, minimum, root.val) and 
                self.isValid(root.right, root.val, maximum))
        
    
    #Solution 2
    """
    def isValidBST(self, root: TreeNode) -> bool:
        #Approach: iterative; but exactly the same under the hood as solutions 3 and 4
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, h is the height of the BST
        
        st = []
        prev = None
        while root or st:
            while root:
                st.append(root)
                root = root.left
