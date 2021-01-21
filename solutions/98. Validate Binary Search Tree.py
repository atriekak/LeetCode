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
        
        #logic
        self.inorder(root.left)
        
        if self.prev and self.prev.val >= root.val:
            self.isValid = False
            #will still get the correct answer if we comment the return out
            #will just traverse through the entire tree each time
            return 
        
        self.prev = root
        
        self.inorder(root.right)
    """
