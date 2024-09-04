n = 12120

def getPallindrom(num):
    num_int = num
    num =str(num)
    
    mid = int(len(num)/2)
    print(mid)
    if str(num_int-1) == getMirror(num_int-1):
        return str(num_int-1)
        
    if len(num)==1:
        return str(int(num)-1)
    if len(num)==2:
        if num[1] == 0:
            return num[0]+num[0]
    
    if num == getMirror(num):
        l = len(num)
        if (num[0]=="9"):
            s = ""
            for i in range(l-1):
                s = s + str(int(num[0]) - 1)
            return s
        else:
            s = ""
            for i in range(l):
                s = s+str(int(num[0])-1)
            return s
        
    if len(num)%2==0:
        print("even")
        mid_part = num[mid-1:mid+1]
        right_part = num[mid+1:len(num)]
        left_part = num[0:mid-1]
        mr = getMirror(right_part)
        ml = getMirror(left_part)
        n1 = left_part +num[mid-1]+num[mid-1] + ml
        n2 = mr + num[mid-1]+num[mid-1]+ right_part
        if abs(num_int-int(n1))>abs(num_int-int(n2)):
            return n2
        else:
            return n1
        
    else:
        right_part = num[mid+1:len(num)]
        left_part = num[0:mid]
        mr = getMirror(right_part)
        ml = getMirror(left_part)
        n1 = left_part+num[mid]+ml
        n2 = mr + num[mid]+right_part
        print(abs(num_int-int(n1)),"-",n1)
        print(abs(num_int-int(n2)),"-",n2)
        if abs(num_int-int(n1))>abs(num_int-int(n2)):
            return n2
        else:
            return n1

def getMirror(num):
    x = str(num)
    x = x[::-1]
    return x

#res = getMirror(12)
#print(res)
res = getPallindrom(100)
print(res)