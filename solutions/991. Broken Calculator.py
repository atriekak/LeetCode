from collections import deque
​
class Solution:
    #Solution 1
    def brokenCalc(self, X: int, Y: int) -> int:
        #Approach: Greedy; working backwards 
        #Time Complexity: log(Y - X) if Y > X else O(1)
        #Space Complexity: O(1)
        
        operations = 0
        while Y > X:
            Y = Y // 2 if Y % 2 == 0 else Y + 1
            operations += 1  
        operations += (X - Y)
        
        return operations
    
    #Solution 2
    """
    def brokenCalc(self, X: int, Y: int) -> int:
        #Approach: BFS
        #Time Complexity: O(2^(Y - X)) if Y > X else O(Y - X)
        #Space Complexity: O(2^(Y - X)) if Y > X else O(Y - X)
        
        de = deque()
        de.append(X)
        
        operations = 0
        while de:
            sz = len(de)
            for _ in range(sz):
                X = de.popleft()
                if X == Y:
                    return operations
                
                de.append(X - 1)
                if X < Y:
                    de.append(2 * X)
                    
            operations += 1
    """
