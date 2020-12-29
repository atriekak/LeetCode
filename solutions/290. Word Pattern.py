class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False
        
        p_dict = {}
        s_dict = {}
        
        for idx in range(len(pattern)):
            if pattern[idx] in p_dict:
                p_dict[pattern[idx]].append(idx)
            else:
                p_dict[pattern[idx]] = [idx]
                
            if s_list[idx] in s_dict:
                s_dict[s_list[idx]].append(idx)
            else:
                s_dict[s_list[idx]] = [idx]
        
        return list(p_dict.values()) == list(s_dict.values())
