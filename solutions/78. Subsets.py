        
        #logic
        #not choose
        self.backtracking(nums, idx + 1, path)
        
        #choose
        path.append(nums[idx])
        self.backtracking(nums, idx + 1, path)
        
        #backtracking
        path.pop()
    """
    
    #Solution 3
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Approach: Recursion
        #Time Complexity: O(n * 2^n)
        #Space Complexity: O(n * 2^n)   // deep copy of path at every node
        #where, n is the length of nums
        
        self.result = []
        self.helper(nums, 0, [])
        return self.result
    
    def helper(self, nums, idx, path):
        #base
        if idx == len(nums):
            self.result.append(path)
            return
        
        #logic
        #not choose
        self.helper(nums, idx + 1, path.copy())
        
        #choose
        path.append(nums[idx])
        self.helper(nums, idx + 1, path.copy())
    """
