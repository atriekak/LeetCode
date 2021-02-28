class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(len(text1) * len(text2))
        #Space Complexity: O(len(text1) * len(text2))
        
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                    
        return dp[-1][-1]
