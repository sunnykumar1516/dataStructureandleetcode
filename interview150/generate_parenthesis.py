# question number 22

def solve(n):
    res = []
    def explore(cur,open,close,n):
        if open==3 and close==3:
            res.append(cur)
            return
        if open<n:
            cur = cur+'('
            explore(cur,open+1,close,n)
        if open>close:
            cur = cur+')'
            explore(cur,open,close+1,n)
            
    explore("",0,0,3)
    
    
    return res

print(solve(3))