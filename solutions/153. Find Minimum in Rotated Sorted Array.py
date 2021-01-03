class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Time Complexity: O(log nums)
        #Space Compllexity: O(1)
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:               #perfectly sorted array
                return nums[l]
            mid = l + (r - l) // 2
            if ((mid == 0 or nums[mid] < nums[mid-1]) and 
                (mid == len(nums) - 1 or nums[mid] < nums[mid+1])):
                return nums[mid]
            elif nums[l] <= nums[mid]:              #only the unsorted side can have min/max
                l = mid + 1                         #move towards it
            else:
                r = mid - 1
        return -1
