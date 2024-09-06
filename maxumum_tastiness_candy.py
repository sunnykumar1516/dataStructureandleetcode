a = [11,12,3,5,6,7,3,5,9]
a.sort()
print(a)
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
def getMaxtase(a):
    a.sort()
    