class Solution:
    def confusingNumber(self, N: int) -> bool:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of the digit N
        
        oldN, newN = N, 0
        rotMap = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        
        while N:
            rem = N % 10
            if rem not in rotMap:
                return False
            newN = newN * 10 + rotMap[rem]
            
            N = N // 10
            
        return newN != oldN
