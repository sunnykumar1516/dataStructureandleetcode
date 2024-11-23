# question number 66
def solve(digits):
    number = 0
    for item in digits:
        number =  number*10 +item
    print(number)
    number = number +1
    res = [int(item) for item in str(number)]
    return res
    
digits = [1,2,3]
solve(digits)