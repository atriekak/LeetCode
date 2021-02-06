class Solution:
    #Solution 1
    def hIndex(self, citations: List[int]) -> int:
        #Approach: Binary Search
        #Time Complexity: O(log n)
        #Space Complexity: O(1)
        #where, n is the length of citations list
        
        n = len(citations)
        
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if citations[mid] >= n - mid and (mid == 0 or citations[mid - 1] < n - (mid - 1)):
                return n - mid
            elif citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
        return 0
    
    #Solution 2
    """
    def hIndex(self, citations: List[int]) -> int:
        #Approach: Linear Search
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of citations list
        
        n = len(citations)
        
        for i in range(n):
            if citations[i] >= n - i:
                return n - i 
        return 0
    """
