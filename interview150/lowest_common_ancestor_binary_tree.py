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
def display_tree(root, level=0):
    if root is not None:
        display_tree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.val)
        display_tree(root.left, level + 1)

display_tree(root,0)

def solve(root,p,q):
    def explore(node):
        if node is None:return None
        print("cuurrent",node.val)
        if node == p:
            return node
        if node == q:
            return node
        left = explore(node.left)
        right = explore(node.right)
        if left and right: return node
        if left is None and right:return right
        if right is None and left:return left
    res = explore(root)
    return res.val

print(solve(root,root.left.left,root.left.right ))
