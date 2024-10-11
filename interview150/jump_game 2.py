# question number 45
def solve(nums):
    jump = 0
    reach = 0
    farthest = 0
    for i in range(len(nums)):
        farthest = max(farthest,i+nums[i])
        if reach==i:
            jump+=1
            reach = farthest
        if farthest>=len(nums)-1:
            jump+=1
            break
    return jump
    
   
nums = [2,3,1,1,4]
nums=[1,2]
print(solve(nums))