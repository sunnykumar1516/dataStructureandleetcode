#question number 14

def solve(strs):
    strs.sort()
    s =''
    for i in range(len(strs[0])):
        if strs[0][i]==strs[len(strs)-1][i]:
            s = s+strs[0][i]
        if strs[0][i]!=strs[len(strs)-1][i]:
            return s
        
strs = ["flower","flow","flight"]
print(solve(strs))