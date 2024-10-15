
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next= n.next

def solve(head):
    
    def explore(node,current):
        
        if not node:
            return False
        if node in current:
            return True
        current.append(node)
        return explore(node.next,current)
    return explore(head,[])
print(solve(n))

