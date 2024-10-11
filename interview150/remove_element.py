# remove element

def solve(nums, val):
    nums.sort()
    p1 = 0
    p2 = len(nums)-1
    while(p1<len(nums)):
        if nums[p1]==val:
            nums[p1]=nums[p2]
            p2-=1
        p1+=1
    print(p2)
    return nums
nums=[1,4,3,2,2,4]
print(solve(nums,2))
