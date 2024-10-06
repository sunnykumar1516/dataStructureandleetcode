# question number 221
def solve(grid):
    m,n = len(grid),len(grid[0])
    res=[[0]*n for _ in range(m)]
    side = 0
    for i in range(m):
        for j in range(n):
            item = grid[i][j]
            if item=='1'and i==0 and j==0:
                res[i][j]=1
            elif item=='1':
                 res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1]) + 1
        side = max(side,max(res[i]))
    print(res)
    print(grid)
    return side
grid = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(solve(grid))