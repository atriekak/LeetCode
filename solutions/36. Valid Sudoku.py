class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Approach: Hashing
        #Time Complexity: O(1) // constant board size
        #Space Complexity: O(1) // constant board size
        
        m = len(board)
        n = len(board[0])
        
        row_map = [set() for i in range(m)]
        col_map = [set() for j in range(n)]
        box_map = [[set() for j in range(n)] for i in range(m)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.':
                    continue
                
                box_i = i // 3
                box_j = j // 3
                
                if val in row_map[i] or val in col_map[j] or val in box_map[box_i][box_j]:
                    return False
                
                row_map[i].add(val)
                col_map[j].add(val)
                box_map[box_i][box_j].add(val)
                
        return True
