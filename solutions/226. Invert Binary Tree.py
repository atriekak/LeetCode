# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Solution 1
    def invertTree(self, root: TreeNode) -> TreeNode:
        #Approach: Flip tree at each node; iterative
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        
        curr = root
        st = []
        while st or curr:
            while curr:
                curr.left, curr.right = curr.right, curr.left
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            curr = curr.right
        
        return root
    
    #Solution 2
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        #Approach: Flip tree at each node; recursive
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        
        self.inorder(root)
        return root
    
    def inorder(self, root):
        #base
        if not root:
            return
        
        #logic
        root.left, root.right = root.right, root.left
        self.inorder(root.left)
        self.inorder(root.right)
    """
