#question number 21
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def solve(l1,l2):
   def explore(l1,l2):
       if l1 is None: return l2
       if l2 is None: return l1
       res = ListNode()
       if l1.val < l2.val:
           res = l1
           res.next= explore(l1.next,l2)
       else:
           res= l2
           res.next = explore(l1,l2.next)
           
       return res
       
       
           
    


