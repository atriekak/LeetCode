class Solution:
    #Solution 1
    def nthUglyNumber(self, n: int) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        uglies = []
        uglies.append(1)
        
        p2, p3, p5 = 0, 0, 0
        n2, n3, n5 = 2, 3, 5
        
        for i in range(1, n):
            minimum = min(n2, n3, n5)
            uglies.append(minimum)
            
            if n2 == minimum:
                p2 += 1
                n2 = uglies[p2] * 2
            if n3 == minimum:
                p3 += 1
                n3 = uglies[p3] * 3
            if n5 == minimum:
                p5 += 1
                n5 = uglies[p5] * 5
        
        return uglies[-1]
    
    #Solution 2
    """
    def nthUglyNumber(self, n: int) -> int:
        #Approach: Priority Queue with HashMap
        #Time Complexity: O(n log n)
        #Space Complexity: O(n)
        
        primes = [2, 3, 5]
        hashset = set()
        heap = []
        
        ugly = 1
        heap.append(ugly)
        hashset.add(ugly)
        
        for i in range(n):
            ugly = heappop(heap)
            
            for prime in primes:
                newUgly = ugly * prime
                if newUgly not in hashset:
                    heappush(heap, newUgly)
                    hashset.add(newUgly)
                    
        return ugly
    """
