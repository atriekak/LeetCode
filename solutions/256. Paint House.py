class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #Time Complexity: O(n) 
        #Space Complexity: O(1)
        #where, n is the number of houses
        #Note: could have also used a length 3 list if mutating the original matrix
        #was not allowed
        #Does not change the space complexity in this case
        
        if len(costs) == 0:
            return 0
        
        for row in range(len(costs) - 2, -1, -1):
            costs[row][0] += min(costs[row + 1][1], costs[row + 1][2])
            costs[row][1] += min(costs[row + 1][0], costs[row + 1][2])
            costs[row][2] += min(costs[row + 1][0], costs[row + 1][1])
        
        return min(costs[0])
