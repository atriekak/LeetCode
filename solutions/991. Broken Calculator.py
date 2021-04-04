class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        #Time Complexity: log(Y - X)
        #Space Complexity: O(1)
        
        operations = 0
        while Y > X:
            Y = Y // 2 if Y % 2 == 0 else Y + 1
            operations += 1  
        operations += (X - Y)
        
        return operations
