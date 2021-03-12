class Solution:
    #Solution 1
    def longestConsecutive(self, nums: List[int]) -> int:
        #Approach: HashSet
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of nums
        #Note: here, traversing over the list instead of the set may be a better choice
        #In that scenario, may want to have a 'visited' set for first elements of sequences
        #due to duplicates
        
        if not nums:
            return 0
        
        numSet = {num for num in nums}
        
        result = 0
        curr = 1
        
        for num in numSet:
            if num - 1 in numSet:
                continue
                
            search = num
            while search + 1 in numSet:
                curr += 1
                search += 1
            
            result = max(result, curr)
            curr = 1
        
        return result
    
    #Solution 2
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        #Approach: Linear traversal after sorting
        #Time Complexity: O(n log n)
        #Space Complexity: O(1)
        #where, n is the length of nums
        
        if not nums:
            return 0
        
        nums.sort()
        
        result = 0
        curr = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            
            elif nums[i] - nums[i - 1] == 1:
                curr += 1
                
            else:
                result = max(result, curr)
                curr = 1
                
        result = max(result, curr)  # clean-up at the end
        
        return result
    """
