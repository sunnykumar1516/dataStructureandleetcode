#question number 77

def solve(n,k):
    res = []
    def explore(index,k,current,n):
        if len(current)==k:
            res.append(current[:])
            return
        
        for i in range(index,n+1):
            current.append(i)
            explore(i+1,k,current,n)
            current.pop()
            
    explore(1,k,[],n)
    return res

n= 4
k= 2
print(solve(n,k))

