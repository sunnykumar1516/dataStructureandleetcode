# question number 383
from collections import Counter as c
def solve(ransomeNote, magazine):
    count_rn = c(ransomeNote)
    count_mg = c(magazine)
    for item in count_rn:
        required_letters = count_rn[item]
        available_letters = count_mg[item]
        if available_letters == 0: return False
        elif available_letters<required_letters: return  False
        else: continue
    return True
        
   
r = "aac"
m="aab"
print(solve(r,m))

