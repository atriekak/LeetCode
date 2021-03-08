class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Approch: Stack  //  Greedy
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of num
        
        st = []
        
        for digit in num:
            while st and st[-1] > digit and k != 0:
                st.pop()
                k -= 1
            
            st.append(digit)
            
        while k != 0:
            st.pop()
            k -= 1
        
        result = ''.join(st)
        result = result.lstrip('0')
        
        return result if result else '0'
