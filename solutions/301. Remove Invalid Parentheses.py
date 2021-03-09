from collections import deque
​
class Solution:
    #Solution 1
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #Approach: BFS
        #Time Complexity: O(2^n * n^2)
        #Space Complexity: O(2^n * n)
        #where, n is the length of the string s
        
        #a little optimization for validity check
        alpha_count = 0
        for char in s:
            if char.isalpha():
                alpha_count += 1
        
        de = deque()
        visited = set()
        result = []
        
        de.append(s)
        visited.add(s)
        
        while de:
            sz = len(de)  # don't actually need since we stop appending after first solution
            for _ in range(sz):
                popped = de.popleft()
                if self.isValid(popped, alpha_count):
                    result.append(popped)
                
                if not result:
                    for i in range(len(popped)):
                        if popped[i].isalpha():
                            continue
                        new = popped[:i] + popped[i+1:]
                        if new not in visited:
                            de.append(new)
                            visited.add(new)
        
        return result
    
    #Solution 2
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #Approach: Backtracking w/ pruning
        #Time Complexity: O(2^n * n^2)
        #Space Complexity: O(2^n * n)   //  because of 'visited'
        #where, n is the length of the string s
        
        #a little optimization for validity check
        self.alpha_count = 0
        for char in s:
            if char.isalpha():
                self.alpha_count += 1
        
        self.result, self.length = [], 0
        self.visited = set()
        
        self.dfs(list(s))
        self.visited.add(s)
        
        return self.result
    
    def dfs(self, sb):
        #base
