class Solution:
    #Solution 1
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #Approach: Sorting, followed by Modified Binary Search
        #Time Complexity: O(n log n)
        #Space Complexity: O(n)
        #where, n is the length of envelopes array
        #note: the problem is reduced to #300 'Longest Increasing Subsequence' after sorting
        
        #need to sort one dimension, and reverse-sort the other
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        eff_seq = []
        
        for e in envelopes:
            if not eff_seq or (eff_seq[-1][0] < e[0] and eff_seq[-1][1] < e[1]):
                eff_seq.append(e)
                
            else:
                idx = self.binarySearch(eff_seq, e[1])
                eff_seq[idx] = e
                
        return len(eff_seq)
    
    def binarySearch(self, arr, target):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid][1] == target:
                return mid
            elif arr[mid][1] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
    
    #Solution 2
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #Approach: Sorting, followed by Dynamic Programming
        #Time Complexity: O(n^2)
        #Space Complexity: O(n)
        #where, n is the length of envelopes array
        
        #only need to sort one dimension
        envelopes.sort(key = lambda x: x[0])
        dp = [1 for _ in envelopes]
        
        result = 1
        for i in range(1, len(dp)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
            
        return result
    """
        
