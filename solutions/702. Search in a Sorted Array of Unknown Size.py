# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
​
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        #Time Complexity: O(log n)
        #Space Complexity: O(1)
        #where, n is the length of nums
        
        l = 0
        r = 1
        while reader.get(r) < target:
            l = r + 1
            r *= 2
        
        while l <= r:
            mid = l + (r - l) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1
