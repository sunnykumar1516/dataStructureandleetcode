# question number 373
import heapq as hp
def solve(a1,a2,k):
    res = []
    pairs =[]
    for i in range(len(a1)):
        for j in range(len(a2)):
            sum = a1[i]+a2[j]
            hp.heappush(res,(sum,i,j))
    while(k>0):
        p = hp.heappop(res)
        pairs.append([a1[p[1]],a2[p[2]]])
        k = k-1
    return pairs
    
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
res = solve(nums1,nums2,k)
print(res)
    