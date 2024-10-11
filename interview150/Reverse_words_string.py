#question number 151
def solve(str):
    a=[]
    word =''
    for i in range(len(str)):
        if str[i] == " " and word !=" ":
            a.append(word.strip())
            word=""
        word= word+str[i]
    for i in range(len(a)-1,-1,-1):
        word = word+" "+a[i]
        
    print(word.strip())
s="  hello  world  "
solve(s)