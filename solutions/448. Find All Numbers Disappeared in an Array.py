class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the size of nums
        
        for num in nums:
            abs_num = abs(num)
            nums[abs_num - 1] = - (abs(nums[abs_num - 1]))
            
        return [i+1 for i in range(len(nums)) if not nums[i] < 0]
