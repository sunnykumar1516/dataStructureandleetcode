# question number 86
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1,ListNode(4,ListNode(3,
                ListNode(2,ListNode(5,ListNode(2))))))

def solve(head,x):
    small = ListNode(-1)
    large = ListNode(-1)
    p1,p2 = small,large
    
    while(head):
        if head.val < x:
            small.next = head
            small= small.next
        else:
            large.next = head
            large = large.next
        head = head.next
        
    large.next = None
    small.next = p2.next
        
    return p1.next
s= solve(head,3)
while(s):
    print(s.val,end="-")
    s = s.next