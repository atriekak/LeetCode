class Solution:
    #Solution 1
    def singleNumber(self, nums: List[int]) -> List[int]:
        #Approach: Bit Manipulation
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of nums
        
        #bitmask would have the combination of both 'single' numbers
        bitmask = 0
        for num in nums:
            bitmask ^= num
            
        #bitwise '& (and)' of diff will give 0 with exactly one of the 'single' numbers
        #-bitmask is the 2's complement of bitmask
        diff = bitmask & (-bitmask)
        
        #thus, bitmask would be equal to one of the 'single' numbers
        bitmask2 = 0
        for num in nums:
            if num & diff != 0:
                print (num)
                bitmask2 ^= num
        
        return [bitmask2, bitmask2 ^ bitmask]
    
    #Solution 2
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
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
        
        return [num for num in numSet]
    """
