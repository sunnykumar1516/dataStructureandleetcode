a = [11,12,3,5,6,7,3,5,9]
def binarysearch_iteration(a,key):
    a.sort()
    print(a)
    length = len(a)
    left,right = 0,length-1
    while(left<=right):
        mid = int((left+right)/2)
        if key == a[mid]:
            return mid
        elif key>a[mid]:
            left = mid+1
        elif key< a[mid]:
            right = mid-1
            
x = binarysearch_iteration(a,6)
print(x)
def binarySearch(l,r,mid,key):
    if key == a[mid]:
        return mid
    if key>a[mid]:
        l= mid+1
        mid = int((l+r)/2)
        return binarySearch(l, r, mid, key)
    elif key<a[mid]:
        r = mid-1
        mid = int((l+r)/2)
        return  binarySearch(l, r, mid, key)
    
l = 0
r = len(a)-1
mid =  int((l+r)/2)
key = 9

#------------------------
def getMaxtaste(a,n):
    length = len(a)
    a.sort()
    start,end = 0,a[length-1]-a[0]
    
    result = 0
    while(start<=end):
        k = 1
        mid = int((start+end)/2)
        element = a[0]
        for i in range(1,length):
            if a[i]-element>=mid:
                k = k+1
                element = a[i]
                
        if k >=n:
            result =  max(mid,result)
            start = mid+1
        else:
            end = mid-1
    
    return result

#a=[13,5,1,8,21,2]
#x = getMaxtaste(a, 3)
#print(x)

#-------------------2nd method

def getMaxTaste(a,n):
    length = len(a)
    a.sort()
    low,high = 0,a[length-1]-a[0]
    last = a[0]
    r=0
    while low<= high:
        mid = int((low + high) / 2)
        count = 1
        for i in range(1,length):
            if a[i]-last >= mid:
                count =  count+1
                last = a[i]
            
        if count>=n:
            r = max(r,mid)
            low = mid+1
        else:
            high = mid-1

    