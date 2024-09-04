import re
import math
f = "-1/2+3/2+1/2"
f = "-1/2+1/2"
f = "-1/2+1/2+1/3"
f = "1/3-1/2"
operator = []
num =[]
den = []
sample = []
delimiters = ["-", "+",""]
lcm = 1
s = re.split('-|\+', f)

        
for item in s:
   
    if item=="":
        continue
    item = item.split("/")
    
    n = int(item[0])
    d = int(item[1])
    lcm  = math.lcm(lcm,d)
    
    num.append(n)
    den.append(d)
    
for i,item in enumerate(f):
    
    if item in delimiters and i==0:
        if item== "-":
            item = item + "1"
            operator.append(int(item))
        else:
            operator.append(1)
    elif item in delimiters:
        if len(operator)==0:
            operator.append(1)
        item = item + "1"
        operator.append(int(item))
s = 0
print(operator)
for i,item in enumerate(operator):
    
    print(item,num[i])
    num[i] = num[i] * item
    s = int(lcm / den[i] * num[i]) + s
    
print(den,num,lcm,"t:-",s,"d:-",lcm)

gcd = math.gcd(s,lcm)
lcm = int(lcm/gcd)
s = int(s/gcd)
fra = str(s)+"/"+str(lcm)

print(fra)




