# question number 64

def solve(grid):
    m, n = len(grid), len(grid[0])
    res = [[0] * n for _ in range(m)]
    res[0][0]= grid[0][0]
    
    for r in range(1,len(grid)):# first col
        res[r][0]= res[r-1][0]+grid[r][0]
        
    for r in range(1,len(grid[0])):
        res[0][r]= res[0][r-1]+grid[0][r]
        
    for row in range(1,len(grid)):
        for col in range(1,len(grid[row])):
            res[row][col]=min(res[row-1][col],res[row][col-1])+grid[row][col]
            
    return res[m-1][n-1]
    
        