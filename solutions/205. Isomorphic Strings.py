class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for idx in range(len(s)):
            if s[idx] in s_dict:
                s_dict[s[idx]].append(idx)
            else:
                s_dict[s[idx]] = [idx]
            
            if t[idx] in t_dict:
                t_dict[t[idx]].append(idx)
            else:
                t_dict[t[idx]] = [idx]
        
        return list(s_dict.values()) == list(t_dict.values())
