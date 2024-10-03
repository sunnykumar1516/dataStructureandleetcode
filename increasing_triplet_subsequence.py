#question number 334

def solve(nums):
    res =[1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            pivot = nums[i]
            if pivot>nums[j]:
                res[i]= max(res[i],res[j]+1)
                if res[i]>2:return True
    return False
# 2nd attempt---------------------------------------------
def solve2(nums):
    res = [False]*len(nums)
    
    for k in range(2,len(nums)):
        mid = nums[k-1]
        a1 = nums[0:k-1]
        a2 = nums[k:]
        lmax= max(a1)
        rmax= max(a2)
        if mid>lmax and rmax>mid:
            return True
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
print(solve2(nums))

        
        
        