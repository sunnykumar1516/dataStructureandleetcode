def solve(s,t):
    count = 0
    start =0
    for i in range(len(t)):
        for j in range(start,len(s)):
            if t[i]==s[j]:
                count = count+1
                start = j+1
                break
    print(count)
    
s = "abc"
t = "ahbgdc"
solve(t,s)
        
    