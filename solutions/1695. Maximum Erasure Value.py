class Solution:
    #Solution 1
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #Approach: Two-pointers with HashSet
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        left = 0
        subarr = set()
        curr = result = 0
        
        for i in range(len(nums)):
            while nums[i] in subarr:
                curr -= nums[left]
                subarr.remove(nums[left])
                left += 1
            
            curr += nums[i]
            subarr.add(nums[i])
            result = max(result, curr)
                
        return result
    
    #Solution 2
    """
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #Approach: Two-pointers with HashMap and totalRunningSum
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        left = 0
        subarr = {nums[0] : 0}
        curr = result = nums[0]
        totalRunningSum = [curr]
        
        for i in range(1, len(nums)):
            totalRunningSum.append(nums[i] + totalRunningSum[i - 1])
                
            if nums[i] in subarr and subarr[nums[i]] >= left:
                left = subarr[nums[i]]
                curr = totalRunningSum[i] - totalRunningSum[left]
            else:
                curr += nums[i]
                result = max(result, curr)
            
            subarr[nums[i]] = i
            
        return result
    """
    
    #Solution 3
    """
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #Approach: Two-pointers with HashMap
        #Time Complexity: O(n^2)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        left = 0
        subarr = {}
        curr = result = 0
        
        for i in range(len(nums)):
            if nums[i] in subarr and subarr[nums[i]] >= left:
                left = subarr[nums[i]] + 1
                curr = sum(nums[left : i + 1])    
            else:
                curr += nums[i]
                result = max(result, curr)
            
            subarr[nums[i]] = i
            
        return result
    """
