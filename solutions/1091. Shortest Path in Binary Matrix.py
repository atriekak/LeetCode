class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #Approach: BFS // Level-Order Traversal
        #Time Complexity: O(n^2)
        #Space Complexity: O(n^2)
        #where, the given grid is of n*n size
        
        n = len(grid)
        dirArr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        de = deque()
        if grid[0][0] == 0:
            de.append((0, 0))
            grid[0][0] = 1
        
        steps = 1
        while de:
            for _ in range(len(de)):
                popped = de.popleft()
                if popped == (n - 1, n - 1):
                    return steps
                for dir in dirArr:
                    r = popped[0] + dir[0]
                    c = popped[1] + dir[1]
                    
                    if r >= 0 and r < n and c >= 0 and c < n and grid[r][c] == 0:
                        de.append((r, c))
                        grid[r][c] = 1
            steps += 1
            
        return -1
