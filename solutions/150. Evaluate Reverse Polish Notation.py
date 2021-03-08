class Solution:
    #Solution 1
    def evalRPN(self, tokens: List[str]) -> int:
        #Approach: Stack, with operations dict
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the total length of tokens
        
        st = []
        op_dict = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b)
        }
        
        for token in tokens:
            if token.lstrip('-').isdigit():
                st.append(int(token))
            
            else:
                pop1 = st.pop()
                pop2 = st.pop()
                op = op_dict[token]
                
                st.append(op(pop2, pop1))
                    
        return st[-1]
    
    #Solution 2
    """
    def evalRPN(self, tokens: List[str]) -> int:
        #Approach: Stack
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the total length of tokens
        
        st = []
        
        for token in tokens:
            if token.lstrip('-').isdigit():
                st.append(int(token))
            
            else:
                pop1 = st.pop()
                pop2 = st.pop()
                
                if token == '+':
                    st.append(pop2 + pop1)
                    
                elif token == '-':
                    st.append(pop2 - pop1)
                    
                elif token == '*':
                    st.append(pop2 * pop1)
                    
                else: #token == '/'
                    st.append(int(pop2 / pop1))
                    
        return st[-1]
    """
