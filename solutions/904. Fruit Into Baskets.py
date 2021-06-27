class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Approach: Sliding Window, HashMap
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the length of the fruits array
        
        countMap = {}
        left = 0
        for i, f in enumerate(fruits):
            countMap[f] = countMap.get(f, 0) + 1
            if len(countMap) > 2:
                countMap[fruits[left]] -= 1
                if countMap[fruits[left]] == 0:
                    del countMap[fruits[left]]
                left += 1
                    
        return i - left + 1
