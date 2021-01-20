                
                if popped.left:
                    de.append(popped.left)
                if popped.right:
                    de.append(popped.right)
            
            result.append(temp)
        
        return result
    
    #Solution 2
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #Approach: DFS, recursive
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
            self.result.append([])
        self.result[level].append(root.val)
        
        self.dfs(root.left, level + 1)
        #st.pop()
        self.dfs(root.right, level + 1)
    """
