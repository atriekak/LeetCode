from collections import deque
​
class Solution:
    #Solution 1
    def closedIsland(self, grid: List[List[int]]) -> int:
        #Approach: DFS
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n)
        #where, the grid is of the shape m * n
        
        self.result = 0
        self.dirArr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.closed = True
                    self.dfs(grid, i, j)
                    if self.closed:
                        self.result += 1
        
        return self.result
    
    def dfs(self, grid, row, col):
        #base
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            self.closed = False
            return
        elif grid[row][col] == 1:
            return
        
        #logic
        grid[row][col] = 1
        
        for dir in self.dirArr:
            i = row + dir[0]
            j = col + dir[1]
            
            self.dfs(grid, i, j)
    
    #Solution 2
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        #Approach: BFS
        #Time Complexity: O(m * n)
        #Space Complexity: O(m * n)
        #where, the grid is of the shape m * n
        
        result = 0
        dirArr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    de = deque()
                    de.append((i, j))
                    grid[i][j] = 1
                    closed = True
                    
                    while de:
                        popped = de.popleft()
                        for dir in dirArr:
                            row = popped[0] + dir[0]
                            col = popped[1] + dir[1]
                            
                            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                                closed = False
                                continue
                            elif grid[row][col] == 1:
                                continue
                            de.append((row, col))
                            grid[row][col] = 1
                    
                    if closed:
                        result += 1
        
        return result
    """
