res = []
def solve(open,close,curr,n):
    if open == n and close == n:
        res.append(curr)
        return
    if open<n:
        curr =  curr+"("
        solve(open+1,close,curr,n)
    if open>close:
        curr = curr+")"
        solve(open,close+1,curr,n)
    
solve(0,0,"",3)
print(res)