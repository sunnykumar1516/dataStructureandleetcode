def bfs(node, visited, grid, count,labels):
    visited[node] = 1
    count_label = [0] * 26
    count_label[ord(labels[node]) - 97] = 1
    #print("node", node, "-lable-", labels[node], "-", count_label)
    for item in grid[node]:
        if visited[item] == 1:
            continue
        #node = item
        x = bfs(item, visited, grid, count,labels)
        for j in range(26):
            count_label[j] += x[j]
    # count[node]=count_label[ord(labels[node])-97]
    count[node] = count_label[ord(labels[node]) - 97]
    return count_label
    
def dfs( node, visited, grid, fst, labels):
        
        visited[node] = 1
        count_label = [0] * 26
        count_label[ord(labels[node]) - 97] = 1
        for item in grid[node]:
            if visited[item] == 1:
                continue
            # node = item
            x = dfs(item, visited, grid, fst, labels)
            for j in range(26):
                count_label[j] += x[j]
        fst[node] = count_label[ord(labels[node]) - 97]
        
        return count_label
def countSubTrees(n, edges, labels):
    grid = [[] for _ in range(n)]
    for i, j in edges:
        grid[i].append(j)
        grid[j].append(i)
    visited = [0] * n
    count = [0] * n
    bfs(0, visited, grid, count,labels)
    #dfs(0, visited, grid, count, labels)
    return count


edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
res = countSubTrees(7, edges, labels)
print(res)