# question number 79
def solve(board,word):
    
    def explore(word,board,row,col,next,index):
        if index+1>len(word):
            return
        if index == len(word):
            return True
        
       
        #move right
        if col+1<len(board) and board[row][col+1]==next:
            next = word[index+1]
            explore(word,board,row,col+1,next,index+1)
        # move left
        if col-1>=0 and board[row][col-1]==next:
            next = word[index + 1]
            explore(word, board, row, col - 1, next, index + 1)
            
        # move down
        if row+1< len(board[0]) and board[row+1][col]==next:
            next = word[index+1]
            explore(word,board,row+1,col,next,index+1)
        # move up
        if row-1 >= 0 and board[row-1][col]== next:
            next = word[index + 1]
            explore(word, board, row - 1, col, next, index + 1)
    
    def explore2(current,word,board,row,col):
        board[row][col]= '-1'
        if current == word:
            return True
        
            
        if col + 1 < len(board[0]) and board[row][col + 1] == word[len(current)]:
            current = current + word[len(current)]
            return explore2(current, word, board, row, col + 1)
            
        if col-1>=0 and board[row][col-1]==word[len(current)]:
            current = current + word[len(current)]
            return explore2(current, word, board, row, col - 1)
        
        if row + 1 < len(board) and board[row+1][col] == word[len(current)]:
            current = current + word[len(current)]
            return explore2(current, word, board, row+1, col)
        
        if row - 1 >= 0 and board[row-1][col] == word[len(current)]:
            current = current + word[len(current)]
            return explore2(current, word, board, row-1, col)
          
    c =""
    for i in range(len(board)):
        for j in range(len(board[0])):
            item = board[i][j]
            if item == word[0]:
                c=c+item
                x = explore2(c,word,board,i,j)
                c =""
                if(x): return True
    return False
                

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"

#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["a","a"]]
word="aa"
board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
word = "AAB"
print(solve(board,word))
    
    
    
    
