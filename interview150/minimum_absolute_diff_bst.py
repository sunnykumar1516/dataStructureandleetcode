# question number 530
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
    prev,diff = None,float('inf')
    def solve(self,root):
        self.prev = None
        self.diff = float('inf')
        def explore(node,min1):
            if node is None:
                return min1
       
            a = explore(node.left,min1)
            print(node.val)
            if self.prev is not None:
                self.diff = min(self.diff, node.val-self.prev)
            self.prev = node.val
            b = explore(node.right,min1)
        explore(root,min1=float('inf'))
        print(self.diff)

s = Solution()
s.solve(root)
