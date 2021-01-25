class Solution:
    #Solution 1
    def findPairs(self, nums: List[int], k: int) -> int:
        #Approach: Hashing
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        hash_map = {}
        count = 0
        for num in nums:
            if k != 0 and num in hash_map:
                hash_map[num] = hash_map.get(num, 0) + 1
                continue
            
            if hash_map.get(num, 0) > 1:
                hash_map[num] = hash_map.get(num, 0) + 1
                continue
            
            complement1 = num + k
            complement2 = num - k
            if complement1 in hash_map:
                count += 1
            if complement2 != complement1 and complement2 in hash_map:
                count += 1
            
            hash_map[num] = hash_map.get(num, 0) + 1
                
        return count
    
    #Solution 2
    """
    def findPairs(self, nums: List[int], k: int) -> int:
        #Approach: Two pointers
        #Time Complexity: O(n log n) // due to sorting
        #Space Complexity: O(1)
        #where, n is the length of nums
        
        nums.sort()
​
        left = 0
        right = 1
    
        count = 0
        while right <= len(nums) - 1 and left <= len(nums) - 2:
            if nums[right] - nums[left] == k:
                count += 1
                left += 1
                right += 1
                while right <= len(nums) - 1 and nums[right] == nums[right - 1]:
                        right += 1
                while left <= len(nums) - 2 and nums[left] == nums[left - 1]:
                    if left + 1 < right:
                        left += 1
                    else:
                        left += 1
                        right += 1
            elif nums[right] - nums[left] > k:
