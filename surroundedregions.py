#https://leetcode.com/problems/surrounded-regions/submissions/
#https://leetcode.com/problems/surrounded-regions/discuss/1553272/Explanation-using-Pictures-oror-DFS-oror-Python
class Solution:
    
    def depth_first_search(self, board, row, col):
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] in 'XV':
            return 
        
        board[row][col] = 'V'
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in moves:
            self.depth_first_search(board, row + dr, col + dc)
    
    
    def solve(self, board: List[List[str]]) -> None:

        rows_num,cols_num = len(board), len(board[0])
        
        # Traversing Grid along the 0th and (n-1)th row
        for col in range(cols_num):
            # 0th row
            if board[0][col] == 'O':
                self.depth_first_search(board, 0, col)
            # (rows_num-1)th row
            if board[rows_num-1][col] == 'O':
                self.depth_first_search(board, rows_num-1, col)
        
        # Traversing Grid along the 0th and (m-1)th column
        for row in range(rows_num):
            # 0th column
            if board[row][0] == 'O':
                self.depth_first_search(board, row, 0)
            # (m-1)th column
            if board[row][cols_num-1] == 'O':
                self.depth_first_search(board, row, cols_num-1)
                
        # post-processing board        
        for row in range(rows_num):
            for col in range(cols_num):
                if board[row][col] == 'V':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'                
