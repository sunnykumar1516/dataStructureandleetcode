# question number 63
def solve(grid):
    m,n= len(grid),len(grid[0])
    res = [[0]*n for _ in range(m)]
    print(res)
    pivot = 1
    
    for r in range(0,len(grid)): # down
        if grid[r][0]==1:
            pivot = 0
            res[r][0] = pivot
        else: res[r][0] = pivot
        
    pivot = 1
    for r in range(0,len(grid[0])):#right
        if grid[0][r]==1:
            pivot =0
            res[0][r]=pivot
        else: res[0][r]=pivot
    
    for row in range(1,m):
        for col in range(1,n):
            if grid[row][col]==1: res[row][col]=0
            else: res[row][col]= res[row-1][col]+res[row][col-1]
    print(res)
        
        
    
grid = [[0,0,0],[0,1,0],[0,0,0]]
solve(grid)
