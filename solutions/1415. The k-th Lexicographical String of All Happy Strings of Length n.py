class Solution:
    #Solution 1
    def getHappyString(self, n: int, k: int) -> str:
        #Approach: Backtracking
        #Time Complexity: O(n * k)
        #Space Complexity: O(n)     // under the hood
        
        self.chars = ['a', 'b', 'c']
        self.count, self.result = 0,  ''
        self.backtrack(n, k, [])
        return self.result
    
    def backtrack(self, n, k, sb):
        #base
        if self.result:
            return
        if len(sb) == n:
            self.count += 1
            if self.count == k:
                self.result = ''.join(sb)
            return
        
        #logic
        for char in self.chars:
            if not sb or sb[-1] != char:
                sb.append(char)                 #action
                self.backtrack(n, k, sb)        #recursion
                sb.pop()                        #backtrack
    
    #Solution 2
    """
    def getHappyString(self, n: int, k: int) -> str:
        #Approach: Backtracking
        #Time Complexity: O(n * k)
        #Space Complexity: O(n * k)
        
        self.chars = ['a', 'b', 'c']
        self.strings = []
        self.backtrack(n, k, [])
        return self.strings[-1] if len(self.strings) == k else ''
    
    def backtrack(self, n, k, sb):
        #base
        if len(self.strings) == k:
            return
        if len(sb) == n:
            self.strings.append(''.join(sb))
            return
        
        #logic
        for char in self.chars:
            if not sb or sb[-1] != char:
                sb.append(char)                 #action
                self.backtrack(n, k, sb)        #recursion
                sb.pop()                        #backtrack
    """
