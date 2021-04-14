class Solution:
    #Solution 1
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Approach: Single stack
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of heights
        
        heights.append(0)   # to pop everything at the end
        st = [-1]           # to calculate the width when nothing else in st
    
        i = 0
        maxAr = 0
​
        while i < len(heights):
            if st[-1] == -1 or heights[st[-1]] <= heights[i]:
                st.append(i)
                i += 1
            else:
                popped = st.pop()
                ar = heights[popped] * (i - st[-1] - 1)
                maxAr = max(maxAr, ar)
            
        return maxAr
    
    #Solution 2
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Approach: Divide and Conquer
        #Time Complexity: O(n^2)    // sorted input; but O(n log n) in avergae case
        #Space Complexity: O(n)
        #where, n is the length of heights
        
        self.maxAr = 0
        self.helper(heights, 0, len(heights) - 1)
        return self.maxAr
    
    def helper(self, heights, low, high):
        #base
        if low > high:
            return
        
        #logic
        idx = low
        for i in range(low, high + 1):
            if heights[i] < heights[idx]:
                idx = i
                
        self.maxAr = max(self.maxAr, heights[idx] * (high - low + 1))
