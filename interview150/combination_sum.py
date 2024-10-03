# question number 39
def solve(arr,target):
     res = []
     def explore(temp,t,start):
         if t==target:
             res.append(temp[:])
             return
         if t>target:
             return
         for i in range(start,len(arr)):
             temp.append(arr[i])
             explore(temp,t+arr[i],i)
             temp.pop()
         
     explore([],0,0)
     return res

arr=[2,3,6,7]
t = 7
print(solve(arr,t))


     
     
     