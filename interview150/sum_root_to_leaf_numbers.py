#question number 129
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

def solve(root):
    res =[]
    def explore(node,curr):
        if node is None:
            return
        curr = curr*10+node.val
        if node.left is None and node.right is None:
            res.append(curr)
            curr = curr-node.val
            return node,curr
        explore(node.left,curr)
        explore(node.right,curr)
    
    explore(root,0)
    print(res)
    print(sum(res))

solve(root)