# question number 8
def getInteger(s):
    d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(s) == 0: return 0
    s = removeLeadingSpace(s)
    num = ""
    pos = False
    neg = False
    digit = False
    for item in s:
        if '+-' in num or '-+' in num:return 0
        
        if item == "0":
            digit = True
            num= num+item
        elif item == "+" or item == "-":
            if(digit):break
            num= num+item
        elif item in d:
            digit = True
            num= num+item
        else:
            break
    print(num)

def removeLeadingSpace(s):
    if s[0] !=" ":
        return s
    
    if s[0]==" ":
        return removeLeadingSpace(s[1:])
    

s = "0-1"
x = getInteger(s)
print(x)