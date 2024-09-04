


def calculate(i,j,size,grid):

    print("start:-",i,j,"kernel size:-",size,grid)
    sum_set = set()
    for r in range(size):
        sum = 0
        for c in range(size):
            item = grid[i+r][j+c]
            sum = sum+item
        sum_set.add(sum)
        if len(sum_set)>1:
            return False
    for c1 in range(size):
        sum = 0
        for r1 in range(size):
            item = grid[i + r1][j + c1]
            sum = sum + item
        sum_set.add(sum)
        if len(sum_set) > 1:
            return False
    # for forward diagonal
    sum = 0
    for x in range(size):
        sum += grid[i + x][j + x]
    sum_set.add(sum)
    if len(sum_set) > 1:
        return False
        
    # for backward diagonal
    sum = 0
    for x in range(size):
        sum += grid[i + x][j + size - 1 - x]
    sum_set.add(sum)
    if len(sum_set) > 1:
        return False
    
    return True
            
        
            
        

def calculateMagicSquare():
    grid = [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
    max_length=min(len(grid),len(grid[0]))
    print(max_length)
    rows = len(grid)
    col = len(grid[0])
    r_mov = (rows-max_length )+1
    c_mov = (col-max_length )+1
    s = max_length
    
    while(s>=2):
        for i in range(r_mov):
            for j in range(c_mov):
                r=calculate(i,j,s,grid)
                print("-----------------")
                print("result:-",r)
                if r:
                    print("current size:-",s)
                    return s
                else:
                    print(r)
                    print("current size:-", s)
        
        s = s-1
        r_mov = (rows - s) + 1
        c_mov = (col - s) + 1
        
    
res = calculateMagicSquare()
print(res)