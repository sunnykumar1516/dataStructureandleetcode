def search(a,e):
    length =  len(a)
    low = 0
    high = length-1
    while(high>=low):
        mid = int((low+high)/2)
        if e == mid:
            return mid
        if e>a[mid]:
            low = mid+1
        elif e<a[mid]:
            high=mid-1
         
a = [0,1,2,3,4,5,6,7]
x = search(a,7)
print(x)