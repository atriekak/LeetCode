class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        running_sum = 0
        max_len = 0
        
        #stores running_sum: index of first occurence
        #initialized to convey balance sum at start
        hash_map = {0: -1}
        
        for i in range(len(nums)):
            running_sum += (1 if nums[i] == 1 else -1)
            
            if running_sum in hash_map:
                max_len = max(max_len, i - hash_map[running_sum])
            else:
                hash_map[running_sum] = i
                
        return max_len
