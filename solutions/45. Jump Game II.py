from collections import deque
​
class Solution:
    #Solution 1
    def jump(self, nums: List[int]) -> bool:
        #Approach: BFS
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        if len(nums) <= 1:
            return 0
        
        jumps = 1
        currLast = nums[0]
        nextLast = nums[0]
        
        if currLast == len(nums) - 1:
            return jumps
        
        for i in range(1, len(nums)):
            nextLast = max(nextLast, i + nums[i])
            
            if currLast == i:
                jumps += 1
                currLast = nextLast
                
            if currLast >= len(nums) - 1:
                break
            
        return jumps
    
    #Solution 2
    """
    def jump(self, nums: List[int]) -> bool:
        #Approach: BFS
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of nums
        
        de = deque()
        visited = set()
        
        de.append(0)
        visited.add(0)
        
        jumps = 0
        while de:
            sz = len(de)
            for _ in range(sz):
                idx = de.popleft()
                if idx == len(nums) - 1:
                    return jumps
                
                for j in range(1, nums[idx] + 1):
                    if idx + j not in visited:
                        de.append(idx + j)
                        visited.add(idx + j)
