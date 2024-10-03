#question number 120

def solve(triangle):
    res=[(0,0)]*len(triangle)
    res[0]=(0,triangle[0][0])
    s = triangle[0][0]
    for i in range(1,len(triangle)):
        index,_ = res[i-1]
        e1,e2 = triangle[i][index],triangle[i][index+1]
        s = res[i][1]
        if e1<e2:
            res[i]=(index,s+e1)
            s = s+e1
        else:
            res[i]=(index+1,s+e2)
            s=s+e2
        
    return s
    
#-----------botttom to up
def solve2(triangle):
    dp = triangle[-1]
    res=[triangle[-1]]
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            item = min(triangle[row][col]+dp[col],triangle[row][col]+dp[col+1])
            dp[col]=item
            
    print(dp)
    print(res)
    return dp[0]
        
    
    


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(solve2(triangle))