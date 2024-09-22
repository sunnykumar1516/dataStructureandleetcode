res = []
def generate(n):
    res = []
    
    
def solve(open,close,n, curr):
    if open == n and close == n:
        res.append(curr)
        return 
    if open<n:
        s = curr+")"
        solve(open, close+1, n, curr)
    
    if close>n:
        s = curr+"("
        solve(open+1, close, n, curr)
