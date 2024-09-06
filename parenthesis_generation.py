res = []
def solve(open,close,curr,n):
    i = 0
    if open == n and close == n:
        res.append(curr)
        return
    if open<n:
        curr =  curr+"("
        solve(open+1,close,curr,n)
    if open>close:
        curr = curr+")"
        solve(open,close+1,curr,n)
        i =i+1
        print("here:-",i)
    
solve(0,0,"",3)
print(res)