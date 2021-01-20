            result.append(temp)
            
        return result
    
    #Solution 2
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Approach: DFS, right-root-left
        #Time Complexity: O(n)
        #Space Complexity: O(h) // under the hood
        
        self.result = []
        
        if not root:
            return self.result
        
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root, level):
        #base
        if not root:
            return
        
        #logic
        if level == len(self.result):
            self.result.append(root.val)
            
        self.dfs(root.right, level + 1)     #going to the right side first
        #st.pop()
        self.dfs(root.left, level + 1)
    """
    
    #Solution 3
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Approach: DFS, left-root-right
        #Time Complexity: O(n)
        #Space Complexity: O(h) // under the hood
        
        self.result = []
        
        if not root:
            return self.result
        
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root, level):
        #base
        if not root:
            return
        
        #logic
        if level == len(self.result):
            self.result.append(root.val)
        else:   #since we are going to the left side first
            self.result[level] = root.val
            
        self.dfs(root.left, level + 1)
        #st.pop()
        self.dfs(root.right, level + 1)
    """
