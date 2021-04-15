class Solution:
    #Solution 1 -- k duplicate removal
    def removeDuplicates(self, s: str, k: int) -> str:
        #Approach: Stack
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        st = []
        for char in s:
            while st and st[-1][1] == k:
                st.pop()
            
            if st and st[-1][0] == char:
                st[-1][1] += 1
            else:
                st.append([char, 1])
        
        if st and st[-1][1] == k:
            st.pop()
        
        sb = []
        for char, count in st:
            sb.extend([char] * count)
        
        return ''.join(sb)
    
    #Solution 2 -- k+ duplicate removal
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        #Approach: Stack
        #Time Complexity: O(n)
        #Space Complexity: O(n)    
    
        st = []
        for char in s:
            while st and st[-1][0] != char and st[-1][1] >= k:
                st.pop()
            
            if st and st[-1][0] == char:
                st[-1][1] += 1
            else:
                st.append([char, 1])
        
        if st and st[-1][1] >= k:
            st.pop()
        
        sb = []
        for char, count in st:
            sb.extend([char] * count)
        
        return ''.join(sb)
    """
