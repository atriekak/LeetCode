class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #Approach: Linear Traversal
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        result = 0
            
        prev_diff = None
        curr_count = 0
        
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            
            if curr_diff == prev_diff:
                curr_count += 1
                result += curr_count
            else:
                curr_count = 0
            
            prev_diff = curr_diff
            
        return result
