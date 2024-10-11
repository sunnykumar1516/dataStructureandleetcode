#question number 112
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
# Create a symmetric binary tree
#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   11
def solve(root, targetSum):
    def explore(node, sum):
        if node is None:
            return False
        sum = sum + node.val
        if node.left is None and node.right is None:
            return sum == targetSum
        
        left = explore(node.left, sum)
        right = explore(node.right, sum)
        
        if left or right:
            return True
    
    res = explore(root, 0)
    return res
    
print(solve(root,6))
   
   
