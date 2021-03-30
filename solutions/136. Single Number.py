class Solution:
    #Solution 1
    def singleNumber(self, nums: List[int]) -> int:
        #Approach: Bit Manipulation
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of nums
        
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        return bitmask
    
    #Solution 2
    """
    def singleNumber(self, nums: List[int]) -> int:
        #Approach: HashSet
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        numSet = set()
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        
        return numSet.pop()
    """
