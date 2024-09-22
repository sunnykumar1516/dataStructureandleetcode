class Solution():
    board  = None
    result = []
    row,col = 0,0
    def solve(self,n):
        print('supplied board',n)
        self.board = [[0 for c in range(n)] for r in range(n)]
        print(self.board)
        self.row = len(self.board)
        self.col = len(self.board)
        x  = self.solvePlacement(0,self.board)
        print("got you",x)
        return self.result
    def solvePlacement(self,row,board):
        if row >= self.row:
            print("solution",board)
            s = [[0 for c in range(self.col)] for r in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    if board[i][j]==1:
                        s[i][j]='q'
            
            self.result.append(s)
            
        for c in range(self.col):
            if (self.validate(row,c,board)):
                board[row][c] = 1
                self.solvePlacement(row+1,board)
                board[row][c] = 0
            
    def validate(self,rows,cols,board):
        print(rows,cols)
        #checking upside
        for r in range(rows-1,-1,-1):
            item = board[r][cols]
            if item == 1:return False
        
        #checking left diagnol
        for i, j in zip(range(rows, -1, -1), range(cols, -1, -1)):
            if board[i][j] == 1:
                return False
               
            
        #checking left diagnol
        for i, j in zip(range(rows, -1, -1), range(cols, self.col)):
            if board[i][j] == 1:
                return False
            
        return True

s = Solution()
x = s.solve(n=4)
print(x)