import heapq as hp
def minOperation(nums,k):
    hp.heapify(nums)
    flag = True
    count = 0
    while(flag):
        x = hp.heappop(nums)
        if x >=k:
            flag = False
        else:
            count = count+1
            y = hp.heappop(nums)
            r = min(x, y) * 2 + max(x, y)
            hp.heappush(nums,r)
    return count

nums = [2,11,10,1,3]
k = 10
nums = [1,1,2,4,9]
k = 20
r=minOperation(nums,k)
print(r)