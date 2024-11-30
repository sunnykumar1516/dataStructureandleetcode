def solve(height):
    length = len(height)
    res = 0
    left = 0
    right = length-1
    while(left<right):
        a = min(height[left],height[right])
        res = max(res,a*(right-left))
        if height[left]<height[right]:
            left = left+1
        else:
            right = right-1
    print(res)



height = [1,8,6,2,5,4,8,3,7]
solve(height)
