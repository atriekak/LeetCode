from collections import deque
​
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Approach: BFS, level-order traversal
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n) // deque
        
        m, n = len(grid), len(grid[0])
        
        fresh = 0
        de = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    de.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = -1
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]    
        while de:
            minutes += 1
            sz = len(de)
            
            for i in range(sz):
                cell = de.popleft()
                for d in dirs:
                    r = cell[0] + d[0]
                    c = cell[1] + d[1]
                    
                    if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1:
                        de.append((r, c))
                        grid[r][c] = 2
                        fresh -= 1
        
        return minutes if fresh == 0 else -1
