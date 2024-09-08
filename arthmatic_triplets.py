#question number 2367
def solve(a,d):
    count = 0
    for n in range(len(a)-1):
        j = a[n]
        i = j-d
        k = j+d
        if i in a[0:n+1] and k in a[n+1:]:
            count = count+1
    return count

a = [0,1,4,6,7,10]
r = solve(a,3)
print(r)