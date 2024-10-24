#question number 215
import heapq as hp
def solve(nums,k):
    hp.heapify(nums)
    res = None
    while(len(nums)>=k):
        res = hp.heappop(nums)
    return res
a= [3,2,1,5,6,4]
res = solve(a,2)
print(res)