class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        #Approach: Greedy
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of lists A and B
        
        a, b = A[0], B[0]
        
        aCount = [0 for _ in range(6)]
        bCount = [0 for _ in range(6)]
        orCount = [0 for _ in range(6)]
        for i in range(len(A)):
            aCount[A[i] - 1] += 1
            bCount[B[i] - 1] += 1
            
            orCount[A[i] - 1] += 1
            if A[i] != B[i]:
                orCount[B[i] - 1] += 1
            
            if max(orCount[a - 1], orCount[b - 1]) < i + 1:
                return -1
        
        result = inf
        for i in range(len(orCount)):
            result = min(result, len(A) - aCount[i], len(B) - bCount[i])
                
        return -1 if result == inf else result
