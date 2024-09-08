class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
def printAll(l):
    flag = True
    while flag:
        if l.next == None:flag = False
        print(l.val)
        l = l.next
def merge(l1,l2):
    l = ListNode()
    while (l1.next != None and l2.next != None):
        v1 = l1.val
        v2 = l2.val
        if v1<=v2:
            l.val= v1
            l.next=ListNode(v2)
        else:
            l.val = v1
            l.next = ListNode(v2)
            
        l1=l1.next
        l2 =l2.next
            
            
            
    
    

    
    
    
l1 =  ListNode(1,ListNode(2,ListNode(3)))
l2 =  ListNode(4,ListNode(5,ListNode(6)))
