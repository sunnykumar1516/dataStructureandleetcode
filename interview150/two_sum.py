# question number 1
def solve(nums,target):
    nums_indices = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in nums_indices:
            return [nums_indices[rem],i]
        else:
            nums_indices[nums[i]] = i
    

nums = [2,7,11,15]
target = 9
res =  solve(nums,target)
print(res)
