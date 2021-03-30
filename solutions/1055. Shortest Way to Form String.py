class Solution:
    #Solution 1
    def shortestWay(self, source: str, target: str) -> int:
        #Approach: Greedy w/ HashMaps
        #Time Complexity: O(m + n)
        #Space Complexity: O(m)
        #where, m and n are the lengths of strings 'source' and 'target' respectively
        
        #stores if and when a character appears next
        charsDict = [None for _ in source]
        for i in reversed(range(len(source))):
            charsDict[i] = {} if i == len(source) - 1 else charsDict[i + 1].copy()
            char = source[i]
            charsDict[i][char] = i
            
        result = 1
        idx = 0     # in source
        
        for char in target:
            #char is in the target string but not the source string
            if char not in charsDict[0]:
                return -1
            
            #char in the source string, but not to the right of idx
            if idx == len(source) or char not in charsDict[idx]:
                result += 1
                idx = 0
                
            #'using up' char at index charsDict[idx][char] in the source string
            idx = charsDict[idx][char] + 1
            
        return result
    
    #Solution 2
    """
    def shortestWay(self, source: str, target: str) -> int:
