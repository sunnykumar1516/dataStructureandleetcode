#question number 228

def solve(nums):
    res=[]
    r1 = nums[0]
    r2 = nums[0]
    for i in range(1,len(nums)):
        if r2+1 == nums[i]:
            r2 = nums[i]
        elif r2+1 != nums[i]:
            #res.append([r1,r2])
            if r1==r2: res.append(str(r2))
            else: res.append(str(r1)+"->"+str(r2))
            
            r1 = nums[i]
            r2= nums[i]
        if i == len(nums)-1:
            if r1 == r2: res.append(str(r2))
            if r1!=r2: res.append(str(r1)+"->"+str(r2))
            
        
            
    print(res)
nums = [0,1,2,4,5,7]
#nums = [0,2,3,4,6,8,9]
solve(nums)
        
        