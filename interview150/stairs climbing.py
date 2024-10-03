# question number 70

def climb(n):
    res = [0,1,2]
    for i in range(3,n+1):
        res.append(res[i-1]+res[i-2])
    return res
print(climb(4))