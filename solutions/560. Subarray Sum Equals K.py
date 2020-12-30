class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        running_sum = 0
        count = 0
        
        #stores running_sum: total occurences of running_sum
        hash_map = {0: 1}
        
        for num in nums:
            running_sum += num
            
            complement = running_sum - k
            count += hash_map.get(complement, 0)
            
            hash_map[running_sum] = hash_map.get(running_sum, 0) + 1
            
        return count
