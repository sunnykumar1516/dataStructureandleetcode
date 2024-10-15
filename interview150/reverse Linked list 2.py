# question number 92
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)
def solve(head,l,r):
    dummy = ListNode(-1)
    dummy.next= head
    prev = dummy
    for i in range(l):
        prev = dummy.next
    current = prev.next
    
    
def reverse(head,left,right):
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    for i in range(left-1):
        print(prev.val)
        prev=prev.next
    current = prev.next
    for i in range(right-left):
        print("+",current.val)
        temp =  current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp
        
    def printMe(node):
        while(node):
            print(node.val,end="-")
            node = node.next
    printMe(dummy.next)
    
   
        
reverse(n,2,4)
        
    
    
    
    
    
        
        
        
