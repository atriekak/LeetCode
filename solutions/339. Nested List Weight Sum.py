# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
​
from collections import deque
​
class Solution:
    #Solution 1
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        #Approach: Recursion / DFS
        #Time Complexity: O(n)
        #Space Complexity: O(d)
        #where, n is the total number of nested elements in the list
        #and, d is the maximum depth in the nestedList
        
        self.result = 0
        self.helper(nestedList, 1)
        return self.result
    
    def helper(self, nestedList, depth):
        for elem in nestedList:
            if elem.isInteger():
                self.result += (elem.getInteger() * depth)
            else:
                self.helper(elem.getList(), depth + 1)
    
    #Solution 2
    """
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        #Approach: BFS
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #where, n is the total number of nested elements in the list
        
        de = deque()
        for elem in nestedList:
            de.append(elem)
        
        depth = 1
        result = 0
        while de:
            for _ in range(len(de)):
                elem = de.popleft()
                if elem.isInteger():
                    result += (elem.getInteger() * depth)
                else:
                    for nestedElem in elem.getList():
                        de.append(nestedElem)
            
            depth += 1
                    
        return result
    """
