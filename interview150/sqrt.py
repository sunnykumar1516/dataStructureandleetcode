# question number 69

def solve(x):
    if x < 2:
        return x
    
    left, right = 1, x//2
    result = 1
    
    while(left<=right):
        mid = (left+right)//2
        if mid*mid == x: # got you
            return mid
        elif mid*mid>x:
            right = mid-1
            #result = mid
        elif mid*mid < x:
            left = mid+1
            result = mid
            
    return result
    
res = solve(8)
print(res)