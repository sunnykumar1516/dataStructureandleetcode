# question number 172

def solve(n):
    x = 5
    sum = 0
    while(n >= x):
        sum = sum+ n//x
        x = x*5
    return sum
n=  100
res = solve(n)
print(res)
