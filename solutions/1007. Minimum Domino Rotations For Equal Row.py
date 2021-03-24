class Solution:
    #Solution 1
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        #Approach: Greedy
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of lists A and B
        
        result = self.check(A, B, A[0])
        if result != -1:
            return result
        return self.check(A, B, B[0])
        
    def check(self, A, B, target):
        aRot = bRot = 0
        for i in range(len(A)):
            if A[i] != target and B[i] != target:
                return -1
            elif A[i] != target:
                aRot += 1
            elif B[i] != target:
                bRot += 1
                
        return min(aRot, bRot)
    
    #Solution 2
    """
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        #Approach: Greedy
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of lists A and B
        
        aCount = [0 for _ in range(6)]
        bCount = [0 for _ in range(6)]
        orCount = [0 for _ in range(6)]
        for i in range(len(A)):
            aCount[A[i] - 1] += 1
            bCount[B[i] - 1] += 1
            
            orCount[A[i] - 1] += 1
            if A[i] != B[i]:
                orCount[B[i] - 1] += 1
            
            if max(orCount) < i + 1:
                return -1
        
        result = inf
        for i in range(len(orCount)):
            result = min(result, len(A) - aCount[i], len(B) - bCount[i])
                
        return -1 if result == inf else result
    """
