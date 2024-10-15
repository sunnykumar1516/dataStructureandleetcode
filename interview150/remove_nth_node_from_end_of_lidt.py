#question number 19
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)
def solve(head,n):
    count = 0
    def explore(node):
        if node is None:
            return 0
        index = explore(node.next)+1
        if index == n:
            node.next = node.next.next
            
        return index
   
    explore(head)
solve(n,2)


