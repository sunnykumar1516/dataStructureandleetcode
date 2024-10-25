# question number 148

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

n = ListNode(4,(ListNode(2,ListNode(1,ListNode(3)))))
while(n):
    print(n.val)
    n = n.next
def solve(head):
    dummy = ListNode(-1)
    dummy.next = head
    p1,p2 = dummy.next,dummy.next
    
