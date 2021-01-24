class Solution {
    int[][]dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    public int[][] updateMatrix(int[][] matrix) {
        if(matrix.length == 0){
            return matrix;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < m;i++){
            for(int j =0 ;j < n;j++){
                if(matrix[i][j] == 0){
                    queue.add(i);
                    queue.add(j);
                }
                if(matrix[i][j] == 1){
                    matrix[i][j] = -1;
                }
            }
        }
        while(!queue.isEmpty()){
            int r = queue.poll();
            int c = queue.poll();
            for(int[]d : dirs){
                int nr = r + d[0];
                int nc = c + d[1];
                if(isSafe(matrix,nr,nc)){
                    if(matrix[nr][nc] == -1){
                        matrix[nr][nc] = matrix[r][c] + 1;
                        queue.add(nr);
                        queue.add(nc);
                     }
                }
            }
        }
        return matrix;
    }
    private boolean isSafe(int[][]matrix,int i,int j){
        return (i >=0 && i < matrix.length && j >= 0 && j < matrix[0].length);
    }
}
