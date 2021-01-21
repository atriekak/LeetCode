    
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
            root = st.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
            
        return True
    """
    
    #Solution 3
    """
    def isValidBST(self, root: TreeNode) -> bool:
        #Approach: recursion; returns validity of BST at that node
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, h is the height of the BST
        
        if not root:
            return True
        
        self.prev = None
        return self.inorder(root)
    
    def inorder(self, root):
        #base
        if not root:
            return True
        
        #logic
        #if we always return, the control won't go to code below
        #but we still have to check the right side if True
        if self.inorder(root.left) == False:
            return False
        
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        
        return self.inorder(root.right)
    """
    
    #Solution 4
    """
    def isValidBST(self, root: TreeNode) -> bool:
        #Approach: recursion; void - returns nothing; but otherwise the same as solution 3
        #Time Complexity: O(n)
        #Space Complexity: O(h)
        #where, h is the height of the BST
        
        if not root:
            return True
        
        self.isValid = True
        self.prev = None
        
        self.inorder(root)
        return self.isValid
        
    def inorder(self, root):
        #base
        if not root:
            return
        
