# question number 55
def solve(nums):
    res=[0]*len(nums)
    res[0]=True
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1):
            if nums[j]+j>=i and res[j]==True:
                res[i]=True
                break
    return res[len(nums)-1]

nums = [2,3,1,1,4]
solve(nums)