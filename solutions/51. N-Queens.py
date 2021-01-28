from copy import deepcopy
​
class Solution:
    #Solution 1
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Approach: Recursion with backtracking
        #Time Complexity: O(n!)
        #Space Complexity: O(n^2) // board; but can be done away with
        #where, n is the either board dimension
        
        result = []
        board = [[0 for j in range(n)] for i in range(n)]
        cols = set()
        upLeft = set()
        upRight = set()
    
        def backtrack(r):
            #base
            if r == len(board):
                ls = []
                for i in range(len(board)):
                    s = ''
                    for j in range(len(board[0])):
                        if board[i][j] == 1:
                            s += 'Q'
                        else:
                            s += '.'
                    ls.append(s)
                result.append(ls)
                return
            
            #logic
            for c in range(len(board[r])):
                if c not in cols and r - c not in upLeft and r + c not in upRight:
                    #action
                    board[r][c] = 1
                    cols.add(c)
                    upLeft.add(r - c)
