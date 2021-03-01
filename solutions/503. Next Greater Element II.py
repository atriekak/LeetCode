class Solution:
    #Solution 1
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Approach: Stack, two-pass; same as solution 2 - concise version
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        n = len(nums)
        result = [-1 for _ in range(n)]
        st = []
        
        #same as solution 2; just reducing the num of lines of code
        for i in reversed(range(2 * n)):
            while st and st[-1] <= nums[i % n]:
                st.pop()
            
            if st:
                result[i % n] = st[-1]
            st.append(nums[i % n])
                    
        return result
    
    #Solution 2
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Approach: Stack, two-pass
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        n = len(nums)
        result = [-1 for _ in range(n)]
        st = []
        
        for i in reversed(range(n)):
            while st and st[-1] <= nums[i]:
                st.pop()
            
            if st:
                result[i] = st[-1]
            st.append(nums[i])
            
        for i in reversed(range(n)):
            while st and st[-1] <= nums[i]:
                st.pop()
            
            if st:
                result[i] = st[-1]
            st.append(nums[i])
                    
        return result
    """
    
    #Solution 3
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Approach: Brute Force, optimized for space
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #where, n is the length of the list T
        
        n = len(nums)
        
        result = [-1 for _ in range(n)]
        for i in range(n):
            for j in range(i, 2*n):
