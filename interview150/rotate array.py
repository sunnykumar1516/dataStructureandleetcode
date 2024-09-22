#question number 189
def solve(nums,k):
     a1 = nums[0:len(nums)-k]
     a2 = nums[len(nums) - k:]
     nums = a2+a1
     return nums
     


nums = [1,2,3,4,5,6,7]
k = 3
x = solve(nums,k)
print(x)