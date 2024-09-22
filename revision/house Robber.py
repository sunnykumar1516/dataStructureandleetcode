def rob(a,n,index):
    if index>=n:
        return 0
    steal = a[index]+rob(a,n,index+2)
    skip = rob(a,n,index+1)
    return max(steal,skip)
    

nums = [1,2,3,1]
x = rob(nums,len(nums),0)
print(x)