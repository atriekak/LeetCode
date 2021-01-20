# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Solution 1
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Approach: BFS
        #Time Complexity: O(n)
        #Space Complexity: O(n) // deque
        
        result = []
        
        if not root:
            return result
        
        de = deque()
        de.append(root)
        
        while de:
            sz = len(de)    #for level-order traversal
            for i in range(sz):
                popped = de.popleft()
                temp = popped.val
                
                if popped.left:
                    de.append(popped.left)
                if popped.right:
                    de.append(popped.right)
            
            result.append(temp)
            
        return result
    
    #Solution 2
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Approach: DFS, right-root-left
        #Time Complexity: O(n)
        #Space Complexity: O(h) // under the hood
        
        self.result = []
        
        if not root:
            return self.result
        
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root, level):
        #base
        if not root:
            return
