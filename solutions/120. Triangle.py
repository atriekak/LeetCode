class Solution:
    #Solution 1
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Approach: Dynamic Programming - bottom-up traversal
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #where, n is the length of triangle
        
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]
    
    #Solution 2
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Approach: Dynamic Programming - top-down traversal
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #where, n is the length of triangle
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
        return min(triangle[-1])
    """
