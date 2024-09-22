
class Solution:
    def solve(self,grid):
        rows,cols = len(grid),len(grid[0])
        count = 0
        
        def navigate(i, j, rows, cols):
            grid[i][j] = '-1'
            # moving right
            if i + 1 < cols and grid[i + 1][j] == "1": navigate(i + 1, j, rows, cols)
            # moving left
            if i - 1 >= 0 and grid[i - 1][j] == "1": navigate(i - 1, j, rows, cols)
            # moving down
            if j + 1 < rows and grid[i][j + 1] == "1": navigate(i, j + 1, rows, cols)
            # moving up
            if j - 1 >= 0 and grid[i][j - 1] == "1": navigate(i, j - 1, rows, cols)
            
        for i in range(rows):
            for j in range(cols):
                item = grid[i][j]
                if item == '1':
                    navigate(i,j,rows,cols)
                    count = count+1
        return count
        
        
        


'''agrid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]'''
s = Solution()
#x = s.solve(grid)
##print(x)

def catchfish(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    def navigate(i,j,rows,cols,count):
        count = count + grid[i][j]
        grid[i][j] = 0
        # moving down
        if i + 1 < rows and grid[i + 1][j] > 0:  navigate(i + 1, j, rows, cols,count)
        # moving up
        if i - 1 >= 0 and grid[i - 1][j]: navigate(i - 1, j, rows, cols,count)
        # moving right
        if j + 1 < cols and grid[i][j + 1] > 0: navigate(i, j + 1, rows, cols,count)
        # moving left
        if j - 1 >= 0 and grid[i][j - 1]> 0: navigate(i, j - 1, rows, cols,count)
        return count
    answer = 0
    for i in range(rows):
        for j in range(cols):
            item = grid[i][j]
            count = 0
            if item > 0:
                x = navigate(i, j, rows, cols,count)
                
                answer =  max(answer,x)
    return answer
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
#grid = [[9,10]]
grid = [[10,5],[8,0]]
#x = catchfish(grid)
#print(x)

def removeDublicate(a):
    res = []
    def navigate(i,item):
        a[i] = -200
        if i+1<len(a) and a[i+1]==item: navigate(i+1,item)
        
    count = 0
    for i in range(len(a)):
        item = a[i]
        if item > -200:
            navigate(i,item)
            count = count+1
            res.append(item)
        print(res)
    return count

nums = [0,0,1,1,1,2,2,3,3,4]
x = removeDublicate(nums)
print(x)
    
    