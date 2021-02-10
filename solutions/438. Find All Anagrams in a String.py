class Solution:
    #Solution 1
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Approach: Sliding Window with HashMap
        #Time Complexity: O(lenS + lenP)
        #Space Complexity: O(1)
        #where, lenS and lenP are the lengths of s and p, respectively
        
        lenS, lenP = len(s), len(p)
        
        map = {}
        for char in p:
            map[char] = map.get(char, 0) + 1
        
        matched, result = 0, []
        for i in range(lenS):
            incoming_char = s[i]
            if incoming_char in map:
                map[incoming_char] = map.get(incoming_char, 0) - 1
                if map[incoming_char] == 0:
                    matched += 1
            
            if i >= lenP:
                outgoing_char = s[i - lenP]
                if outgoing_char in map:
                    if map[outgoing_char] == 0:
                        matched -= 1
                    map[outgoing_char] = map.get(outgoing_char, 0) + 1
            
            if matched == len(map):
                result.append(i - lenP + 1)
        
        return result
    
    #Solution 2
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Approach: Linear Search with HashMap
        #Time Complexity: O(lenS * lenP)  --  time limit exceed
        #Space Complexity: O(1)
        #where, lenS and lenP are the lengths of s and p, respectively
        
        lenS, lenP = len(s), len(p)
        
        pMap = {}
        for char in p:
            pMap[char] = pMap.get(char, 0) + 1
        
        result = []
        for i in range(lenS - lenP + 1):
            subMap = {}
            for char in s[i : i + len(p)]:
                subMap[char] = subMap.get(char, 0) + 1
            
            if subMap == pMap:
                result.append(i)
        
        return result
    """ 
    
    #Solution 3
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Approach: Backtracking, followed by Linear Search
        #Time Complexity: O(X * (lenS - lenP) * lenP)  --  time limit exceed
        #Space Complexity: O(1)
        #where, lenS and lenP are the lengths of s and p, respectively
