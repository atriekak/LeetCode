class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #TimeComplexity: O(numRows^2)
        #SpaceComplexity: O(1)
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        triangle = [[1],[1,1]]
        
        for row in range(3, numRows + 1):
            prev = triangle[-1]
            curr = [1 for i in range(row)]
            
            for i in range(1, len(curr) - 1):
                curr[i] = prev[i-1] + prev[i]
            
            triangle.append(curr)
            
        return triangle
