def findSubSequence(nums):
    res = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            pivot = nums[i]
            if pivot>nums[j]:
                res[i]= max(res[i],res[j]+1)
    return res
        
    
    
    

nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
#nums=[4,10,4,3,8,9]
print(findSubSequence(nums))