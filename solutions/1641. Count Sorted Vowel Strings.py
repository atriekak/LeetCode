class Solution:
    #Solution 1
    def countVowelStrings(self, n: int) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        vowels = 5
        dp = [[1 for _ in range(n+1)] for _ in range(vowels)]
        
        for i in range(1, vowels):
            for j in range(1, n+1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
    
    #Solution 2
    """
    def countVowelStrings(self, n: int) -> int:
        #Approach: Brute force / Bactracking
        #Time Complexity: O(n^5)
        #Space Complexity: O(n)
        
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.result = 0
        self.backtracking([], n, 0)
        return self.result
    
    def backtracking(self, sb, n, idx):
        #base
        if idx == len(self.vowels):
            return
        if len(sb) == n:
            self.result += 1
            return
            
        #logic
        #not choose
        self.backtracking(sb, n, idx + 1)       #recursion
        
        #choose
        sb.append(self.vowels[idx])             #action
        self.backtracking(sb, n, idx)           #recursion
        sb.pop()                                #backtracking
    """
