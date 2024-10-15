#question number 206

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
n = ListNode(1)
n.next=ListNode(2)
n.next.next=ListNode(3)
def solve(node):
    if node.next is None: return node
    last = solve(node.next)
    print(node.val)
    node.next.next = node
    node.next = None
    return last

print(solve(n))

    
    
solve(n)

