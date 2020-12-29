class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #where, n equals min(pattern.length, s.length)
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False
        
        p_dict = {}
        s_dict = {}
        
        for i in range(len(pattern)):
            if pattern[i] in p_dict:
                if p_dict[pattern[i]] != s_list[i]:
                    return False
            else:
                p_dict[pattern[i]] = s_list[i]
                
            if s_list[i] in s_dict:
                if s_dict[s_list[i]] != pattern[i]:
                    return False
            else:
                s_dict[s_list[i]] = pattern[i]
        
        return True
