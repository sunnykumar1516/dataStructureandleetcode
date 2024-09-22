
class Solution():
    board = None
    def solve(self,board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if col == 0 or col == len(board[0])-1 or row == 0 or row == len(board)-1:
                    item = board[row][col]
                    if item == "O":
                        board = self.navigate(board,row,col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "b":
                    board[row][col] = "O"
                else: board[row][col] = "X"
                
        
        return board
        
    def navigate(self,board,row,col):
        board[row][col] = "b"
        if row + 1 < len(board) and board[row+1][col] == "O": self.navigate(board,row+1,col)
        if row - 1 >= 0 and board[row - 1][col] == "O": self.navigate(board, row - 1, col)
        if col + 1 < len(board[0]) and board[row][col+1] == "O": self.navigate(board, row,col+1)
        if col - 1 >= 0 and board[row][col-1] == "O": self.navigate(board, row, col-1)
        
        return board
       


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

s = Solution()
x = s.solve(board)
print(x)