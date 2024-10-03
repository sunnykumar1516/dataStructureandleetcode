#question number 46
def solve(nums):
    res=[]
    def explore(temp):
        if len(temp)== len(nums):
            res.append(temp[:])
            return
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                explore(temp)
                temp.pop()
    explore([])
    
    return res

n = [1,2,3]
print(solve(n))
        
        
