height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = [2,3,4,5,18,17,6]
def maxWater(h):
    hleft,hright,area = None,None,None
    
    lindex = 0
    rindex = len(h)-1
    
    hleft = h[lindex]
    hright = h[rindex]
    width = rindex - lindex
    area = min(hleft,hright)*width
    for i in range(len(h)):
        
        hi = h[i]
        hi2 = h[rindex-i]
        if hi > hleft:
            width = rindex - i
            a = min(hi,hright)*width
            if a>area:
                hleft = hi
                lindex = i
                area = a
                
        if hi2 > hright and rindex>=lindex:
            width = rindex - lindex
            a = min(hleft, hi2) * width
            if a>area:
                hright = hi2
                rindex = rindex-1
                area = a
            
                
    print(area)
    
            
            
def maxwater2(h):
    l = 0
    r = len(h)-1
    area = 0
    while(r>l):
        a = min(h[l],h[r])*(r-l)
        area =  max(a,area)
        if h[l]<h[r]:
            l = l+1
        elif h[l]>=h[r]:
            r = r-1
    return area
    
    
maxwater2(height)
    