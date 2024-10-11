# question number 222
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(10)
def solve(root):
    
    def explore(node,count):
        if node is None:
            return 0
        
        left = explore(node.left,count)
        right = explore(node.right,count)
        return left+right+1
        
    res = explore(root,0)
    return res

print(solve(root))
    
