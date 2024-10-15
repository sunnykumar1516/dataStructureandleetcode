class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def preOrder(root):
    if root is None: return
    print(root.val,end="-")
    left = preOrder(root.left)
    right = preOrder(root.right)

def inOrder(root):
    if root is None: return
    
    left = inOrder(root.left)
    print(root.val,end="-")
    right = inOrder(root.right)

def postOrder(root):
    if root is None: return
    left = inOrder(root.left)
    right = inOrder(root.right)
    print(root.val, end="-")
    
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)