class Solution:
    #Solution 1
    def longestPalindrome(self, s: str) -> str:
        #Approach: Two Pointers
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #where, n is the length of string s
        
        self.maxLength, self.start = 1, 0
        
        for i in range(len(s)):
            self.extendAroundPivot(s, i, i)
            if i + 1 < len(s):
                self.extendAroundPivot(s, i, i + 1)
            
        return s[self.start : self.start + self.maxLength]
    
    def extendAroundPivot(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        left += 1
        right -= 1
        
        if right - left + 1 > self.maxLength:
            self.maxLength = right - left + 1
            self.start = left
    
    #Solution 2
    """
    def longestPalindrome(self, s: str) -> str:
        #Approach: Dynamic Programming
        #Time Complexity: O(n^2)
        #Space Complexity: O(n^2)
        #where, n is the length of string s
        
        dp = [[False for _ in s] for _ in s]
        maxLength, start, end = 1, 0, 0
        
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i - j + 1 > maxLength:
                        maxLength = i - j + 1
                        start, end = j, i
        
        return s[start : end + 1]
    """
    
    #Solution 3
    """
    def longestPalindrome(self, s: str) -> str:
        #Approach: Brute Force
        #Time Complexity: O(n^3)
        #Space Complexity: O(1)
        #where, n is the length of string s
        
        maxLength, start, end = 1, 0, 0
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.isPalindrome(s, i, j) and j - i + 1 > maxLength:
                    maxLength = j - i + 1
                    start, end = i, j
        
        return s[start : end + 1]
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    """
