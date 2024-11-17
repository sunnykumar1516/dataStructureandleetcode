# question number 53

def solve(arr):
    sum = arr[0]
    temp = sum
    for i in range(1,len(arr)):
        temp = max(arr[i],temp+arr[i])
        if temp > sum:
            sum = temp
    return sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
res = solve(arr)
print(res)
