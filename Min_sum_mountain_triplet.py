# question number 2908

def solve(a):
    res = []
    for n in range(1,len(a)-1):
        j = a[n]
        i = min(a[0:n+1])
        k = min(a[n+1:])
        if j>i and j>k:
            res.append(i+j+k)
    return min(res)

a =[8,6,1,5,3]
x = solve(a)
print(x)