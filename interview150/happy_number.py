# question number 202
def solve(n):
    buffer = set()
    while n != 1 and n not in buffer:
        n =  sum( int(digit)**2 for digit in str(n))
        buffer.add(n)
    return  n==1
        
