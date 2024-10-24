# question number 98
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
    flag = None
    prev = None
    def solve(self,root):
        self.flag,self.prev = None,None
        def explore(node):
            if node is None:
                return
            explore(node.left)
            if self.prev is not None and self.flag is None and self.prev>node.val:
                self.flag = False
            self.prev = node.val
            explore(node.right)
        explore(root)
        self.flag = True if self.flag is None else self.flag
        return self.flag
    
s = Solution()
res = s.solve(root)
print(res)
            