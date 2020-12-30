class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n is the length of string
        
        hash_set = set()
        count = 0
        
        for char in s:
            if char in hash_set:
                hash_set.remove(char)
                count += 2
            else:
                hash_set.add(char)
        
        return count + 1 if hash_set else count
