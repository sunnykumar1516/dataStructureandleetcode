#quesrion number 124
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
def solve(root):
    maxSum = float("-inf")
    def explore(node):
        if node is None:return 0
        left = explore(node.left)
        right=explore(node.right)
        
        root_is_best = left+right+node.val
        right_or_left = max(left,right)+node.val
        only_root = node.val
        
        maxSum = max(root_is_best,right_or_left,only_root)
        
        return max(only_root,right_or_left)
        