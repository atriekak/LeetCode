class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        idx = 0
        curr = total = 0
        
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            total += gas[i] - cost[i]
            
            if curr < 0:
                idx = i + 1
                curr = 0
        
        return idx if total >= 0 else -1
