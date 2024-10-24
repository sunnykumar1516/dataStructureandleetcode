# question number 230
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

class Solution:
    res = 0
    def solve(self,root,k):
        self.res = 0
        def explore(node,count,k):
            print(k)
            if node is None:
                return k
            k = explore(node.left,count,k)
            k = k-1
            if k == 0:
                print("k val:-",k)
                self.res = node.val
                
            return explore(node.right,count,k)
            
            
        explore(root,0,k)
        print("final:-",self.res)

s = Solution()
s.solve(root,2)