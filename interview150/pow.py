# question number 50

def solve(x,n):
    x1 = abs(n)
    res = x**x1
    if n < 0: res = float(1/res)
    return res

res =  solve(2,-2)
print(res)