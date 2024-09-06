# question 5

s = "ccabaccabababababa"
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
def checkPallindrom(s): # check pallindrom using iteration
    length = len(s)
    flag = False
    for i in range(length):
        j = length-i-1
        if i<=j:
            if s[i]!=s[j]:
                return False
    return True
    
    
def checkPallindromRec(s,i,j):#check pallindrom using recursion
    if i>=j:
        return True
    if s[i]==s[j]:
       return checkPallindromRec(s, i + 1, j - 1)
    else:
        return False
        
def findLongestPallindrom(s):
    maxLen = 0
    result = ""
    cache = []
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            print(i,j)
            sub = s[i:j]
            res = checkPallindromRec(sub,0,len(sub)-1)
            if res:
                if len(sub)>maxLen:
                    #cache.clear()
                    cache.append([i, j])
                    maxLen = len(sub)
                    result = sub
            
    return result,maxLen,cache
def checkcache(cache,i,j):
    for item in cache:
        if item[0]>i and item[1]<=j:
            return True
    return False
        
#r=checkPallindrom(s)
#r = checkPallindromRec(s,0,len(s)-1)
l,m,c = findLongestPallindrom(s)
print(l,m,c)

    
