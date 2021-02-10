class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Approach: Linear Search
        #Time Complexity: O((lenH - lenN) * lenN)
        #Space Complexity: O(1)
        #where, lenH and lenN are the lengths of haystack and needle, respectively
        
        lenH, lenN = len(haystack), len(needle)
        
        for i in range(lenH - lenN + 1):
            if self.isMatch(haystack, needle, i):
                return i
            
        return -1
    
    def isMatch(self, str1, str2, i):
        for j in range(len(str2)):
            if i + j >= len(str1) or str1[i + j] != str2[j]:
                return False
        
        return True
