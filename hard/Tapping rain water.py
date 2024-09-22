#question number 42

def solve(a):
    leftmax = [0]*len(a)
    rightmax = [0]*len(a)
    l = a[0]
    r = a[len(a)-1]
    for i in range(1,len(a)):
        leftmax[i] = l
        l = max(a[i],l)
    for i in range(len(a)-2,0,-1):
        rightmax[i] = r
        r = max(r,a[i])
        
    water = 0
    for i in range(len(a)):
        height = a[i]
        level = min(leftmax[i],rightmax[i])
        trapped_water = level-height
        if trapped_water >0:
            water =  water+ level-height
        
        
    return water

a = [0,1,0,2,1,0,1,3,2,1,2,1]
a =[4,2,0,3,2,5]
x = solve(a)
print(x)