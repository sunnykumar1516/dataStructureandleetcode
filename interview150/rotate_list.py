# question number 61
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
n.next.next.next.next = ListNode(5)

n2 = ListNode(0,ListNode(1,ListNode(2)))
def solve(head,k):
    
    def getLength(node):
        if node is None:
            return 0
        res = getLength(node.next)+1
        return res
    
    res = getLength(head)
    print("Length:-",res)
    
    index = abs(res - k)
    if k>res:
        i = k%res
        index = res-i
    current = head
    for i in range(index-1):
        current = current.next
    print("getting:-",current.val)
    
    
    temp = current.next
    current.next = None
    dummy = ListNode(-1)
    dummy.next = temp
    while(temp.next):
        temp = temp.next
    temp.next = head
    return dummy.next
   
res = solve(n2,4)
#print(res.val)
while(res):
    print(res.val)
    res = res.next