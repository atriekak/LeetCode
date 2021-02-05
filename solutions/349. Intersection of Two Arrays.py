class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Approach: Hash Map
        #Time Complexity: O(m + n)
        #Space Complexity: O(min(m, n))
        #where m is the length of nums1 and n is the length of nums2
        
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)     #reducing space complexity
        
        countMap = set()
        result = []
        for num in nums1:
            countMap.add(num)
        
        for num in nums2:
            if num in countMap:
                result.append(num)
                countMap.remove(num)
        
        return result
