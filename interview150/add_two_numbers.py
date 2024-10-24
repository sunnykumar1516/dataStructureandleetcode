# question number 2
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
n1 = ListNode(2,ListNode(4,ListNode(9)))
n2 = ListNode(5,ListNode(6,ListNode(9)))

def addTwoNumbers(n1,n2):
    sum = ListNode(-1)
    index = sum
    def explore(node1,node2,sum,carry):
        if node1 is None and node2 is None:
            return carry,sum
        n1 = 0 if node1 is None else node1.val
        n2 = 0 if node2 is None else node2.val
        result = n1+ n2+carry
        carry = 0
        if result>9:
            carry = result//10
            result = result%10
        sum.next= ListNode(result)
        
        index1 = None if node1 is None else node1.next
        index2 = None if node2 is None else node2.next
        
        return  explore(index1,index2,sum.next,carry)
    carry,res = explore(n1,n2,sum,0)
    if carry != 0:
        res.next=ListNode(carry)
    print(carry,res.val)
    return index.next
sum = addTwoNumbers(n1,n2)

while(sum):
    print(sum.val,end="-")
    sum = sum.next

