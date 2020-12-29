class Solution:
    def primeProduct(self, string):
        product = 1
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        for char in string:
            product *= primes[ord(char) - ord('a')]
        return product
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Time Complexity: O(n * k)
        #Space Complexity: O(n * k)
        #where, n equals strs.length, and k equals the average length of a string in strs
        #note that, using the sotred string key results in O(n * k log k) time complexity
        
        out = {}
        for string in strs:
            #key = "".join(sorted(string))
            key = self.primeProduct(string)
            if key in out:
                out[key].append(string)
            else:
                out[key] = [string]
        return list(out.values())
