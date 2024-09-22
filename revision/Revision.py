#Median of Two Sorted Arrays
def medianSortedArray(l1,l2):
    m = l1+l2
    m.sort()
    length = len(m)
    mid =int(length/2)
    if len%2 == 0:
        return (m[mid]+m[mid-1])/2
    else: return m[mid-1]
    
def median_BNS(l1,l2):
    length1 = len(l1)
    length2 = len(l2)
    if length1>length2: l1,l2 = l2,l1
    length1 = len(l1)
    length2 = len(l2)
    print(l1,"-",l2)
    low,high = 0,len(l1)
    right_total = int((length1+length2+1)/2)
    while low<=high:
        mid = int((low + high) / 2)
        e1 , e2 = mid, right_total-mid
        
        
       # left bucket
        if e1 == 0:a = float('-inf')
        else:a = l1[e1 - 1]
        if e2 ==0:b = float('-inf')
        else:b = l2[e2-1]
    # right bucket
        if e1 == length1:c = float('inf')
        else: c = l1[e1]
        if e2 == length2: d = float('inf')
        else:d  = l2[e2]
        
        if a<=d and c>=b:
            if (length1+length2)%2 == 0:
                return (max(a,b)+max(c,d))/2
            else:
                return max(a,b)
        elif a>d:
            high = mid-1
        elif b<d:
            low = mid+1
            
l1 = [1,2]
l2 = [3,4]
x = median_BNS(l1,l2)
print(x)