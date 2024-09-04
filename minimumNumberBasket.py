from collections import Counter
class Solution:
    def minGroupsForValidAssignment(self, nums):
        ct = Counter(nums)
        vs = ct.values()
        mnmx= min(vs)+1

        def search(mn):
            ans = 0
            for i, v in enumerate(vs):
                groups, remain = divmod(v, mn)
                if  remain == 0 :
                    ans += groups + (0 if remain==0 else 1)
                elif remain>0:
                    if mn-remain <=1 and mn - remain-groups <= 1:
                        print("process:-",mn - remain-groups)
                        ans += groups + (0 if remain==0 else 1)
                    else:
                        print("process2:-", mn - remain - groups)
    
                        return -1
            return ans

        for mn in range(mnmx, 0, -1):
            ans = search(mn)
            if ans>0: return ans
        return -1

s = Solution()
a = [1,2,3,1,1,3,1,3] # 5
#a= [1,1,3,3,1,1,2,2,3,1,3,2] #5
r = s.minGroupsForValidAssignment(a)
print(r)