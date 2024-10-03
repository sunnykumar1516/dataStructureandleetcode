# question number 198
def rob(nums):
    res = []
    res.append(nums[0])
    res.append(max(nums[0],nums[1]))
    for i in range(2,len(nums)):
        res.append( max(res[i-2]+nums[i],res[i-1]))
        
    return res

nums = [1,2,3,1]
print(rob(nums))
