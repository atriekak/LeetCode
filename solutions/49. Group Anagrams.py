class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in out:
                out[key].append(string)
            else:
                out[key] = [string]
        return list(out.values())
