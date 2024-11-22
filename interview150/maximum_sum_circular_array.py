# question number 918

def solve(arr):
   def maxSum(arr):
       global_sum = arr[0]
       local_sum = arr[0]
       for i in range(1,len(arr)):
           local_sum = max(arr[i],local_sum+arr[i])
           if local_sum > global_sum:
               global_sum = local_sum
       return global_sum
   def minSum(arr):
       global_sum = arr[0]
       local_sum = arr[0]
       for i in range(1,len(arr)):
           local_sum = min(arr[i], arr[i]+local_sum)
           if local_sum < global_sum:
                global_sum = local_sum
               
       return global_sum
   
   s = sum(arr)
   s1 = maxSum(arr)
   s2 = s - minSum(arr)
   if s1>0:
        return max(s1,s2)
   else:
       return s1
    
   
           
arr =[-3,-2,-3]
res = solve(arr)
print(res)
