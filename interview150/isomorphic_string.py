# question number 205
from collections import Counter as c
def solve(s,t):
    length = len(s)
    s = c(s)
    t = c(t)
    a1 = [s[item] for item in s]
    a2 = [t[item] for item in t]
    print(a1,a2)
    if a1==a2: return True
    else: return False
s = "paper"
t = "title"
print(solve(s,t))