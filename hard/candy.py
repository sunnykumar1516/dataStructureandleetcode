#question 135

def solve(a):
    left = [1] * len(a)
    right = [1] * len(a)
    
    for i in range(len(a)):
        if a[i] > a[i - 1]:
            left[i] = max(left[i], left[i - 1] + 1)
    for i in range(len(a) - 2, -1, -1):
        if a[i] > a[i + 1]:
            right[i] = max(right[i], right[i + 1] + 1)
    sum = 0
    for i in range(len(left)):
        sum = sum + max(left[i], right[i])
    print(left)
    print(right)
    return sum
    
    
   
        
a = [1,0,2]
a = [1,2,2]
a =[1,3,2,2,1]
a = [29,51,87,87,72,12]
x=solve(a)
print(x)