        
        if not root.left and not root.right and currSum == self.target:
            self.result.append(path)
            
        self.helper(root.left, currSum, path.copy())
        self.helper(root.right, currSum, path.copy())
    """
    
    #Solution 3
    """
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        #Approach: Iterative w/ backtracking
        #Time Complexity: O(n) // visiting every node exactly once
        #Space Complexity: O(h) // path can only be as long as the height
        
        result = []
        
        if not root:
            return result
        
        st = []
        currSum = 0
        path = []
        while root or st:
            while root:
                currSum += root.val
                path.append(root.val)
                st.append((root, currSum, path.copy())) #remove copy() when backtracking
                
                root = root.left
            
            root, currSum, path = st.pop()
            if not root.left and not root.right and currSum == sum:
                result.append(path.copy())
            
            root = root.right
            
        return result
    """
