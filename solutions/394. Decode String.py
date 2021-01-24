class Solution:
    i = 0
    
    def decodeString(self, s: str) -> str:
        #Approach: DFS, recursion
        #Time Complexity: O(n * max(k)) //length of the decoded string
        #Space Complexity: O(n) // under the hood
        #where, n is the the length of the encoded string, and 
        #k are the multiplication factors
        
        if not s:
            return s
        
        currNum = 0
        currStr = ''
        
        while self.i < len(s):
            char = s[self.i]
            
            if char.isdigit():
                currNum = currNum * 10 + int(char)
                self.i += 1
            
            elif char.isalpha():
                currStr += char
                self.i += 1
                
            elif char == '[':
                self.i += 1
                
                innerStr = self.decodeString(s)
                for k in range(currNum):
                    currStr += innerStr
                
                currNum = 0
            
