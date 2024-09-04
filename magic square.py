grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
grid = [[5,5,5],[5,5,5],[5,5,5]]
grid = [[10,3,5],[1,6,11],[7,9,2]]
def calulate(grid):
    rows = len(grid)
    cols =  len(grid[0])
    count = 0
    r = 0
    c = 1
    sq = [[0,0,0],[0,0,0],[0,0,0]]
    r_movement = rows - 3
    c_movement = cols - 3
    for i in range(r_movement+1):
        for j in range(c_movement+1):
            r =i
            c = j
            r = calculateSum(r,c,grid,rows*cols)
            if r:
                count = count+1
    print(count)
    
    


def calculateSum(r,c,grid,total):
    flag = False
    distinctElement = []
    
    for i in range(3):#----checking distinct and value<=15
        for j in range(3):
            item = grid[i + r][j + c]
            if (item not in distinctElement) and 0 < item <= 9:
                distinctElement.append(item)
                if len(distinctElement)==total:
                    flag = True
            elif item in distinctElement or item>9 or item<0:
                return False
    
    
    r1 = grid[r][c]+grid[r][c+1]+grid[r][c+2]
    r2 = grid[r+1][c] + grid[r+1][c + 1] + grid[r+1][c + 2]
    r3 = grid[r+2 ][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]
    if (r1==r2==r3):
        flag = True
    else:
        return False
    c1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
    c2 = grid[r][c+1] + grid[r + 1][c+1] + grid[r + 2][c+1]
    c3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c +2]
    if (r1==r2==r3 and r1 == c1==c2==c3):
        flag = True
    else:
        return False
    d1 = grid[r][c]+ grid[r+1][c+1] + grid[r+2][c+2]
    d2 = grid[r][c+2] + grid[r + 1][c + 1] + grid[r+2][c]
    if (r1==r2==r3 and r1 == c1==c2==c3 and r1==d1==d2):
        flag = True
    else:
        return False
    
    return flag
    
    
    
   
    

calulate(grid)