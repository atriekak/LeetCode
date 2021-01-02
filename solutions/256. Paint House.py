class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if len(costs) == 0:
            return 0
        
        for row in range(len(costs) - 2, -1, -1):
            costs[row][0] += min(costs[row + 1][1], costs[row + 1][2])
            costs[row][1] += min(costs[row + 1][0], costs[row + 1][2])
            costs[row][2] += min(costs[row + 1][0], costs[row + 1][1])
        
        return min(costs[0])
