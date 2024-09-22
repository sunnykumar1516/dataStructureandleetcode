def solve(gas,cost):
     total =0
     res = 0
     if sum(gas)<sum(cost):
         return -1
     for i in range(len(gas)):
         earn = gas[i]
         gc = cost[i]
         total = total+ earn - gc
         if total<=0:
             res = i+1
             total = 0
        
             
         
 
 
 