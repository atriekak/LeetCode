class Solution:
    def countArrangement(self, n: int) -> int:
        #Approach: Recursion with backtracking
        #Time Complexity: O(k) ; alternatively, can be thought of as O(n!) even with pruning
        #Space Complexity: O(n) // path, pathMap, recursion stack
        #where, k is the number of valid permutations
        
        self.result = 0
        self.helper([], set(), 1, n)
        return self.result
​
    def helper(self, path, pathMap, idx, n):
        if len(path) == n:
            self.result += 1
​
        #logic
        for i in range(1, n + 1):
            if (i % idx == 0 or idx % i == 0) and i not in pathMap:
                path.append(i)                              #action
                pathMap.add(i)                              #action
​
                self.helper(path, pathMap, idx + 1, n)      #recursion
​
                path.pop()                                  #backtrack
                pathMap.remove(i)                           #backtrack
