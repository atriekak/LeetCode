class Solution:
    #Solution 1
    def maximalSquare(self, matrix):
        #Approach: Dynamic Programming
        #Time Complexity: O(m * n)
        #Space Complexity: 
        #where, the given matrix is of size m * n
        
        maxLen = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                
                maxLen = max(maxLen, matrix[i][j])
        
        return maxLen**2
    
    #Solution 2
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #Approach: Brute Force
        #Time Complexity: O((m*n) ^ 2)
        #Space Complexity: O(1)
        
        maxLen = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    sqlen = 1
                    flag = True
                    while i + sqlen < len(matrix) and j + sqlen < len(matrix[0]) and flag:
                        for k in range(i, i + sqlen + 1):
                            if matrix[k][j + sqlen] == '0':
                                flag = False
                                break
                        
                        for k in range(j, j + sqlen + 1):
                            if matrix[i + sqlen][k] == '0':
                                flag = False
                                break
                                
                        if flag:
                            sqlen += 1
                            
                    maxLen = max(maxLen, sqlen)
