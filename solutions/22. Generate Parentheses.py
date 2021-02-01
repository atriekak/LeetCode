class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Approach: Recursion with backtracking
        #Time Complexity: O(2^2n)
        #Space Complexity: O(n)
        #where, n is the pairs of parentheses
        
        self.result = []
        self.backtrack([], 0, 0, n)
        return self.result
    
    def backtrack(self, path, i, j, n):
        #base
        if i > n or j > i:
            return
        if i == n and j == n:
            self.result.append(''.join(path))
            return
        
        #logic
        path.append('(')                    #action
        self.backtrack(path, i+1, j, n)     #recursion
        del path[-1:]                       #backtracking
        
        path.append(')')                    #action
        self.backtrack(path, i, j+1, n)     #recursion
        del path[-1:]                       #backtracking
    
    """
    def generateParenthesis(self, n: int) -> List[str]:
        #Approach: Recursion with backtracking
        #Time Complexity: O(2^2n)
        #Space Complexity: O(n * 2^2n)
        #where, n is the pairs of parentheses
        
        self.result = []
        self.helper('', 0, 0, n)
        return self.result
    
    def helper (self, path, i, j, n):
        #base
        if i > n or j > i:
            return
        if i == n and j == n:
            self.result.append(path)
            return
        
        #logic
        self.helper(path + '(', i+1, j, n)
        self.helper(path + ')', i, j+1, n)
