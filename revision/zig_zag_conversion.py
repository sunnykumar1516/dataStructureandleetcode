def solve(s,n):
    down = True
    up = False
    res = [[] for i in range(n)]
    i = 0
    for item in s:
        if down:
            res[i].append(item)
            i = i+1
            if i == n:
                down= False
                i = n-1
        else:
            i = i-1
            res[i].append(item)
            if i == 0:
                down = True
                i = 1
    print(res)
    
s = "PAYPALISHIRING"
numRows = 3
solve(s,numRows)
        
        
    
    
    
