class Solution:
    
    def numIslands(self, grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    print(grid[i][j])
                    self.foo(i,j,grid)
                    count+=1
        return count
    def foo(self,idx,idy,grid):
            print("calling", idx ," ",idy)
            grid[idx][idy]='0'
            if idx-1>=0 and grid[idx-1][idy]=='1': self.foo(idx-1,idy,grid)
            if idx+1<len(grid) and grid[idx+1][idy]=='1': self.foo(idx+1,idy,grid)
            if idy-1>=0 and grid[idx][idy-1]=='1': self.foo(idx,idy-1,grid)
            if idy+1<len(grid[0]) and grid[idx][idy+1]=='1': self.foo(idx,idy+1,grid)
            
grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
s = Solution()
x = s.numIslands(grid)
print(x)
