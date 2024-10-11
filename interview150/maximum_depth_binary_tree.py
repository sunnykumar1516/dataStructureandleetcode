# question number 104
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def solve(root):
    res=[]
    def explore(node):
        if node.left==None or node.right==None:
            return
        if node.left:explore(node.left)
        if node.right:explore(node.right)
   