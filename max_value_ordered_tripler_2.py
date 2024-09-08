#question number:2874
# 1st attempt
def solve1(a):
   
    res = []
    res.append(0)
    res.append(0)
    res.append((a[0] - a[1]) * a[2])
    if len(a) < 4:
        answer = res[2]
        if answer < 0:
            return 0
        else:
            return answer
    answer = res[2]
    left = a[2]
    for l in range(3, len(a)):
        n = l
        i = max(a[0:n - 1])
        index1 = a.index(i)
        j = min(a[index1:n])
        
        left = max(a[n],left)
        k = left
        r = (i - j) * k
        res.append(r)
        answer = max(answer, r)
        print(res)
    
    if answer < 0:
        return 0
    else:
        return answer


def solve(a):
    res = []
    res.append(0)
    res.append(0)
    i = a[0]
    j = a[1]
    k = a[2]
    value = (i-j)*k
    res.append(value)
    answer = 0
    for n in range(3,len(a)):
        print("subarray:-",a[0:n])
        if a[n]>k:
            k = a[n]
        if a[n-1]<j:
            j = a[n-1]
        if a[n-2]>i:
            i = a[n-2]
        r = (i-j)*k
        answer = max(answer, r)
        res.append(r)
        print(res)
    if answer < 0:
        return 0
    else:
        return answer
    
#----------------3rd attempt

def solve3(a):
    res = []
    res.append(0)
    res.append(0)
    res.append((a[0] - a[1]) * a[2])
    index = 2
    for i in range(3,len(a)):
        if a[i-1] < a[index]:
            index = i-1
            j = a[i-1]
        else:
            j = a[index]
        k = max(a[index:i+1])
        s = max(a[0:index+1])
        r = (s-j)*k
        res.append(r)
        print(res)
        
#----------------------------------------
def solve4(a):
    ans = 0
    res = []
    for n in range(1,len(a)-1):
        i = max(a[0:n+1])
        j = a[n]
        k = max(a[n+1:])
        r = (i-j)*k
        res.append(r)
        ans = max(ans,r)

def solve5(a):
    res, max_i, max_i_minus_j = 0, 0, 0
    for item in a:
        res = max(res,max_i_minus_j*item)
        max_i_minus_j = max(max_i_minus_j,max_i-item)
        max_i = max(max_i,item)

a = [12,6,1,2,7]
#a = [15,12,2,14,15,18,15,20,14,5,14,14,11,13,7]
#a = [1,10,3,4,19]
#a = [8,6,3,13,2,12,19,5,19,6,10,11,9]
solve5(a)
