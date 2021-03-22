class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Approach: Backtracking
        #Time Complexity: Exponential
        #Space Complexity: O(E)
        #where, E is the number of edges or tickets
        
        tMap = defaultdict(list)
        for fr, to in tickets:
            tMap[fr].append(to)
        
        for key in tMap:
            tMap[key].sort()
        
        self.result = None
        self.backtrack(tMap, ['JFK'], len(tickets))
        return self.result
​
    def backtrack(self, tMap, path, n):
        #base
        if self.result:
            return
        
        if len(path) == n + 1:
            self.result = path.copy()
            return
        
        #logic
        curr = path[-1]
        for i in range(len(tMap.get(curr, []))):
            city = tMap[curr].pop(i)                #action
            path.append(city)
            
            self.backtrack(tMap, path, n)           #recursion
            
            tMap[curr].insert(i, city)              #backtrack
            path.pop()
