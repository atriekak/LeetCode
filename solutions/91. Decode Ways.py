class Solution:
    #Solution 1
    def numDecodings(self, s: str) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        if len(s) == 0:
            return 0
        
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1 
        
        for i in range(2, len(dp)):
            if s[i - 1] != '0':                     #single digit is possible
                dp[i] = dp[i - 1]
            
            if 10 <= int(s[i-2 : i]) <= 26:         #double digit is possible
                dp[i] += dp[i - 2]
​
        return dp[-1]
    
    #Solution 2
    """
    def numDecodings(self, s: str) -> int:
        #Approach: Recursion with/without backtracking
        #Time Complexity: O(2^n)
        #Space Complexity: O(n)
        #where, n is the length of the string
        
        #The solution goes over time limit
        
        self.result = 0
        self.helper(s, [], 0)
        return self.result
    
    def helper(self, s, path, idx):
        #base
        if idx == len(s):
            self.result += 1
            return
        if s[idx] == '0':
            return
        
        #logic
        for i in range(idx, min(idx + 2, len(s))):
            if 1 <= int(s[idx : i + 1]) <= 26:
                path.append(int(s[idx : i + 1]))    #action -- don't need the step
            
                self.helper(s, path, i + 1)         #recursion
                
                path.pop()                          #backtracking -- don't need the step
    """
