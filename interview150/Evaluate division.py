#question number 399

def calculate(eq,val,q):
     adjlist= {}
     i = 0
     res =[]
     for u,v in eq:
         if u not in adjlist:adjlist[u]=[]
         if v not in adjlist:adjlist[v]=[]
         
         adjlist[u].append((v,val[i]))
         adjlist[v].append((u, 1/val[i]))
         i = i+1
     print(adjlist)
     for item in q:
         s,e = item
         v = []
         cost = 1.0
         if e not in adjlist:
             res.append(-1)
         else:
             x = dfs(s,e,v,adjlist,cost)
             res.append(x)
         
     return res
def dfs(start,end,visited,adjlist,cost):
    if start == end:
        return cost
    visited.append(start)
    for node in adjlist.get(start,[]):
        next,c = node
        if next not in visited:
            
            x = dfs(next,end,visited,adjlist,cost*c)
            if x!= -1.0:
                return x

    return -1.0

eq = [["a","b"],["b","c"]]
val = [2.0,3.0]
q=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
x = calculate(eq,val,q)
print(x)