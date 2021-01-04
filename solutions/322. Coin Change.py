class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Time Complexity: O(amount * coins.length) 
        #Space Complexity: O(amount * coins.length)
        
        dp = [[float('inf') for a in range(amount + 1)] for c in range(len(coins) + 1)]
        dp[0][0] = 0
​
        for c in range(1,len(dp)):
            for a in range(len(dp[0])):
                if coins[c-1] > a:
                    dp[c][a] = dp[c-1][a]
                else:
                    dp[c][a] = min(dp[c-1][a], 1 + dp[c][a-coins[c-1]])
        
        return dp[-1][-1] if dp[-1][-1] < float('inf') else -1
