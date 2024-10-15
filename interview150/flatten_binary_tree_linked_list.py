# question number 114

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
def solve(root):
    prev = None
    def explore(node):
        if node is None:
            return
        explore(node.left)
        explore(node.right)
        
        temp= node.right
        node.right = node.left
        node.left = None
        current = node
        while current.right:
            current= current.right
        current.right= temp
    
    explore(root)
        
solve(root)