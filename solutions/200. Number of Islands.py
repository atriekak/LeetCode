from collections import deque
​
class Solution:
    #Solution 1
    def numIslands(self, grid: List[List[str]]) -> int:
        #Approach: DFS, recursive
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n)
        
        m = len(grid)
        n = len(grid[0])
        
        dirArr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        count = 0
        
        def dfs(r, c):
            #base
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != '1':
                return
            
            #logic
            grid[r][c] = '0'
            for d in dirArr:
                dfs(r + d[0], c + d[1])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
               
        return count
    
    #Solution 2
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        #Approach: BFS
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n)
        
        m = len(grid)
        n = len(grid[0])
        
        dirArr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
