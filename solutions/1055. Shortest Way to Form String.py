class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        #Approach: Greedy w/ two pointers
        #Time Complexity: O(m * n)
        #Space Complexity: O(1)
        #where, m and n are the lengths of strings 'source' and 'target' respectively
        
        s = 0
        t = tPrev = 0
        
        result = 0
        while t < len(target):
            while s < len(source) and t < len(target):
                if target[t] == source[s]:
                    t += 1
                s += 1
            
            if t == tPrev:
                return -1
            
            tPrev = t
            s = 0
            result += 1
            
        return result
