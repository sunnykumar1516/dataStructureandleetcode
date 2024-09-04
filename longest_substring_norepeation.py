

def getSubString(s):
    print(s)
    main_sub = []
    maxLen = 0
    t2 = ""
    for i in range(len(s)):
        if s[i] in t2:
            index = t2.find(s[i])
            main_sub.append(t2)
            if index+1<= len(t2):
                t2 = t2[index+1:]+s[i]
            else:
                t2 = ""
        else:
            t2 = t2 + s[i]
            l = len(t2)
            if l>maxLen:maxLen = l
            
            print(t2)
    print(main_sub , maxLen)
 
s = "abcabcbb"
#s="au"
#s ="dvdf"
#s = "anviaj"
#s = "aabaab!bb"
getSubString(s)