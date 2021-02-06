class Solution:
    #Solution 1
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Approach: Hash Map
        #Time Complexity: O(m + n)
        #Space Complexity: O(min(m, n))
        #where m is the length of nums1 and n is the length of nums2
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)     #reducing space complexity
        
        countMap = {}
        result = []
        for num in nums1:
            countMap[num] = countMap.get(num, 0) + 1
        
        for num in nums2:
            if countMap.get(num, 0) > 0:
                result.append(num)
                countMap[num] = countMap.get(num, 0) - 1
        
        return result
    
    #Solution 2
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Approach: Binary Search; for when the arrays are given sorted
        #Time Complexity: O(min(log m + n, m + log n))      //exluding sorting
        #Space Complexity: O(1)
        #where m is the length of nums1 and n is the length of nums2
        
        n1, n2 = len(nums1), len(nums2)
        
