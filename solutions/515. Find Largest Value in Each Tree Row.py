# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
from collections import deque
​
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        #Approach: BFS
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        
        result = []
​
        if not root:
            return result
​
        de = deque()
        de.append(root)
​
        while de:
            sz = len(de)
            temp = - float('inf')
​
            for i in range(sz):
                popped = de.popleft()
                temp = max(temp, popped.val)
​
                if popped.left:
                    de.append(popped.left)
                if popped.right:
                    de.append(popped.right)
            
            result.append(temp)
        
        return result
        
    #Solution 2
    """
    def largestValues(self, root: TreeNode) -> List[int]:
        #Approach: DFS
        #Time Complexity: O(n)
        #Space Complexity: O(h) // under the hood
        #where, h is the height of the tree
​
        self.result = []
​
        if not root:
            return self.result
​
        self.dfs(root, 0)
        return self.result
​
    def dfs(self, root, level):
        #base
        if not root:
            return
​
        #logic
        if len(self.result) == level:
            self.result.append(root.val)
        else:
            self.result[level] = max(self.result[level], root.val)
​
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
    """
