class Solution:
    def myAtoi(self, s: str) -> int:
        #Approach: Linear Traversal
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where n is the length of the string 's'
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        i = 0
        positive = True
        num = 0
        
        while i < len(s) and (s[i] == ' '):
            i += 1
            
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            positive = True if s[i] == '+' else False
            i += 1
            
        while i < len(s) and s[i].isdigit():
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and int(s[i]) > INT_MAX % 10):
                return INT_MAX if positive else INT_MIN
            
            num = num * 10 + int(s[i])
            i += 1
            
        return num if positive else -num
