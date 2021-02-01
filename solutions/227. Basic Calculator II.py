class Solution:
    def calculate(self, s: str) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        self.calc = 0
        self.tail = 0
        
        curr = 0
        op = '+'
        
        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                curr = curr * 10 + int(char)
            else:   #char is an operator
                self.helper(curr, op)
                curr = 0
                op = char
        
        self.helper(curr, op)   #end of string
        return self.calc
        
    def helper(self, curr, op):
        if op == '+':
            self.calc += curr
            self.tail = curr
            
        elif op == '-':
            self.calc -= curr
            self.tail = -curr
        
        elif op == '*':
            self.calc = (self.calc - self.tail) + self.tail * curr
            self.tail *= curr
            
        else: #op == '/'
            if self.tail >= 0:
                self.calc = (self.calc - self.tail) + floor(self.tail / curr)
                self.tail = floor(self.tail / curr)
            else:
                self.calc = (self.calc - self.tail) + ceil(self.tail / curr)
                self.tail = ceil(self.tail / curr)
