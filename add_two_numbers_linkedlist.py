class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node = ListNode(1,ListNode(2,(ListNode(3))))

def printme(node):
    flag = True
    while flag:
        if node.next:
            print(node.val)
            node=node.next
        else:
            print(node.val)
            flag = False
        

node2 = ListNode(10,ListNode(11,(ListNode(12))))
def reverse(head):
    if head.next is None:
        return head
    node = reverse(head.next)
    head.next.next = head
    head.next = None
    return node

    



    

n = reverse(node2)
print(n.val)
printme(n)
#print(node)
