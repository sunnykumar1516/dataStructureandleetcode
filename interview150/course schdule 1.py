class Solution(object):
    visited, inRec = None, None
    res = []
    
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        if len(prerequisites) == 0: return [i for i in range(numCourses)]
        self.res = []
        preq = prerequisites
        adjList = {}
        for item in preq:
            u = item[1]
            v = item[0]
            if u not in adjList:
                adjList[u] = []
            adjList[u].append(v)
        #verifying it has all nodes
        if len(adjList)!=n:
            for i in range(n-1,0,-1):
                if i not in adjList:
                    adjList[i] = []
                    
        self.visited = [0] * numCourses
        self.inRec = [0] * numCourses
        print(adjList)
        for item in adjList:
            if self.visited[item] == 0:
                x = self.dfs(adjList, item)
                if x: return []
        print(self.res)
        return self.res[::-1]
        # -----------------------------
    
    def dfs(self, adjList, u):
        
        self.visited[u] = 1
        self.inRec[u] = 1
        
        for item in adjList.get(u, []):
            if self.inRec[item] == 1:
                return True
            if self.visited[item] == 0:
                if (self.dfs(adjList, item)):
                    return True
        
        self.res.append(u)
        self.inRec[u] = 0
        return False
a = [[1,0],[2,0],[3,1],[3,2]]
a = [[1,0]]
n = 3
s  = Solution()
x = s.findOrder(n,a)
print(x)