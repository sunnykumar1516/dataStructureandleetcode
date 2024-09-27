# question number 54

def solve(mat):
    head= [(0,0)]
    flag = 'm_right'
    rows = len(mat)
    cols = len(mat[0])
    s1 = 0
    s2 =0
    for row in range(s1,rows):
        for col in range(s2,cols):
            if flag == 'm_right':
                print(mat[row][col], end=" ")
                if col == cols-1:
                    flag = 'm_down'
                    s1 = rows
                    break
            elif flag == 'm_left':
                i = rows-row-1
                j = cols-col-1
                print(mat[row][j], end=" ")
                if col == 0:
                    flag = 'm_up'
            elif flag =='m_down':
                i = rows - row - 1
                j = cols - col - 1
                print(mat[row][col], end=" ")
                if row ==  rows-1:
                    flag = 'm_left'
                break
            elif flag == 'm_up':
                i = rows - row - 1
                print(mat[i][col], end=" ")
                break
        print("")
        
        

def solve2(mat):
    result = []
    rows = len(mat)
    cols =len(mat[0])
    while(mat):
        result = result+ mat.pop(0)
        
        if mat and mat[0]:
            for row in mat:
                result.append(row.pop())
                    
        if mat:
            last = mat.pop(len(mat)-1)
            result = result+last[::-1]
            
        if mat and mat[0]:
            for row in mat[::-1]:
                result.append(row.pop(0))
        
    print(result)
        
        
        
   
        

mat = [[1,2,3],[4,5,6],[7,8,9]]
mat =[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
solve2(mat)