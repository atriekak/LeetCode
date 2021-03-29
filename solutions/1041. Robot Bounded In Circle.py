class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #Approach: Linear Traversal
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of instructions
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # arranged in clockwise order
        x = y = 0                                   # starting coordinates
        dir = 0                                     # starting direction
        
        for char in instructions:
            if char == 'L':
                dir = (dir + 3) % 4
            elif char == 'R':
                dir = (dir + 1) % 4
            else:   # char == 'G'
                x += dirs[dir][0]
                y += dirs[dir][1]
        
        #the robot is bounded IF AND ONLY IF we
        #either come back to the origin
        #or the end direction is NOT the same as the start direction
        return x == y == 0 or dir != 0
