class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #Approach: Sliding Window (monotonically non-decreasing)
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k-= 1
                
            if k < 0:
                left += 1
                if nums[left - 1] == 0:
                    k += 1
            
        return right - left + 1
    
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        #Approach: Sliding Window
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        left, zeros = 0, 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > k:
                left += 1
                if nums[left - 1] == 0:
                    zeros -= 1
                    
            result = max(result, right - left + 1)
            
        return result
    """
