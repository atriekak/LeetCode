class Solution:
    #Solution 1
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #Approach: Stack
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of the list T
        
        result = [0 for _ in range(len(T))]
        st = []
        for i in reversed(range(len(T))):
            while st and T[st[-1]] <= T[i]:
                st.pop()
            
            if st:
                result[i] = st[-1] - i
            st.append(i)
                    
        return result
    
    #Solution 2
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #Approach: Brute Force
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #where, n is the length of the list T
        
        result = [0 for _ in range(len(T))]
        for i in range(len(T)):
            for j in range(i, len(T)):
                if T[j] > T[i]:
                    result[i] = j - i
                    break
                    
        return result
    """
