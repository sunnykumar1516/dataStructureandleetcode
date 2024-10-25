#question number 108

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def solve(nums):
    
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = solve(nums[0:mid])
    root.right = solve(nums[mid+1:])
    
    return root
    

