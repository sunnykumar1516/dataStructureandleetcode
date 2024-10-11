#question number 88
def solve(nums1,m,nums2,n):
    [nums1.append(0) for _ in range(n)]
    p1,p2,p = m-1,n-1,m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]>=nums2[p2]:
            nums1[p]=nums1[p1]
            p1-=1
        elif nums2[p2]>nums1[p1]:
            nums1[p]=nums2[p2]
            p2-=1
        p -=1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1
    return nums1
            
            
            
 
nums1 = [1,2,4]
m = 3
nums2 = [1,2,3]
n = 3
print(solve(nums1,m,nums2,n))