class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #Approach: Hashing
        #Time Complexity: O(n)
        #Space Complexity: O(1)     // since only 26 alphabets
        
        hash_set = set()
        for char in s:
            if char in hash_set:
                hash_set.remove(char)
            else:
                hash_set.add(char)
                
        return len(hash_set) <= 1
