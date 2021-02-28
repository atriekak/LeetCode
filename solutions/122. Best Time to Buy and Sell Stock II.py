class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Approach: Linear traversal
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of prices
        
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
                
        return result
