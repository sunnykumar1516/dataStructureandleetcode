
def validate(n,edges,source,destination):
    #creating adjacency list
    adjList = {}
    for i in range(len(edges)):
        item = edges[i]
        u = item[0]
        v= item[1]
        
        if u not in adjList:
            adjList[u] = []
        adjList[u].append(v)
        if v not in adjList:
            adjList[v] = []
        adjList[v].append(u)
    print(adjList)
    
    visited = [0]*n
    
    x =  dfs(0,2,adjList,visited)
        
    return x
def dfs(u,v,adjList,visited):
    if u == v:
        return True
    if visited[u] == 1:
        return False
    visited[u] = 1
    for item in adjList.get(u,[]):
        x = dfs(item, v, adjList, visited)
        if x :return True
    return False

edges = [[0,1],[1,2],[2,0]]
n = 3
source = 0
destination = 2
x =validate(n,edges,source,destination)
print(x)