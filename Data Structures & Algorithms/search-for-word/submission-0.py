class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]

        def helper(i,r,c):
            if i == len(word)-1:
                return True

            ch = board[r][c]
            board[r][c] = '#'
            for dir in dirs:
                n_r = r+dir[0]
                n_c = c+dir[1]

                if n_r<0 or n_c<0 or n_r>=ROWS or n_c>=COLS or board[n_r][n_c] == '#':
                    continue
                
                if board[n_r][n_c] == word[i+1]:
                    if helper(i+1, n_r, n_c):
                        return True
            
            board[r][c] = ch
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if helper(0, i, j):
                        return True
        return False

            
            
