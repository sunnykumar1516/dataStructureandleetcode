
def rob(a):
    length = len(a)
    low = 0
    high = sum(a)
    r = 0
    while(low<=high):
        steal = False
        mid = int((low+high)/2)
        rem = mid
        for i in range(length):
            if steal:
                steal = False
                continue
                
            if rem>a[i]:
                rem = rem - a[i]
                steal = True
                
        if rem>0:
            low = mid+1
        else:
            
            r =  max(r,mid)
            
            
    return r





#---------2nd attempt
def robHouse(a):
    
    money = []
    money.append(a[0])
    money.append(max(a[0],a[1]))
    for i in range(2,len(a)):
        m = max(a[i]+money[i-2],money[i-1])
        money.append(m)
    print(money)
    return money[len(money)-1]

nums = [1,2,3,1]
x=robHouse(nums)
print(x)