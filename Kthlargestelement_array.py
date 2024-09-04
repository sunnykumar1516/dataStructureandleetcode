import heapq as hp
def kLargest(nums,k):
    
    hp.heapify(nums)
    while len(nums)>k:
        hp.heappop(nums)
    return nums[0]

nums = [3,2,1,5,6,4]
k = 2
res=kLargest(nums,k)
print(res)