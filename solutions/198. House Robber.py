class Solution:
    def rob(self, nums: List[int]) -> int:
        #Time Complexity: O(nums) 
        #Space Complexity: O(nums)
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1]
