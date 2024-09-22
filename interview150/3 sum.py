
def find3sum(a):
    res = []
    a.sort()
    pairs = []
    for i in range(3,len(a)):
        for j in range(i):
            sum = a[i]+a[j]
            if sum*-1 in a[0:i-j-1] or sum*-1 in a[j+1:i]:
                pairs.append(a[i])
                pairs.append(a[j])
                pairs.append(sum*-1)
                pairs.sort()
                if pairs not in res:
                    res.append(pairs)
                pairs = []
    
    return res

a = [1,2,-2,-1]
a = [-1,0,1,2,-1,-4]

x = find3sum(a)
print(x)
    