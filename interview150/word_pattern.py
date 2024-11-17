# question number 290
from collections import Counter as c
def solve(pattern,s):
    res = {}
    buffer = c(pattern)
    print(buffer)
    s = s.split()
    s = c(s)
    print(s)
    
    
    
pattern = "abba"
s = "dog cat cat dog"
solve(pattern,s)