class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #Approach: Backtracking
        #Time Complexity: O(n * 2^n)
        #Space Complexity: O(n)
        #where n is the length of the string s
        
        self.n = len(s)
        self.result = 0
        self.set = set()
        self.backtrack(s, 0)
        return self.result
    
    def backtrack(self, s, idx):
        #base
        if idx == self.n:
            self.result = max(self.result, len(self.set))
            return
        
        #logic
        for i in range(idx + 1, self.n + 1):
            currS = s[idx : i]
            if currS not in self.set:
                self.set.add(currS)                 #action
                self.backtrack(s, i)                #recursion
                self.set.remove(currS)              #backtrack
