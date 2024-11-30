# question number 201

def solve(left,right):
    left_bit = bin(left)[2:].zfill(32)
    right_bit = bin(right)[2:].zfill(32)
    print(left_bit,right_bit)
    count = 0
    for i in range(32):
        count+=1
        left = left>>1
        right = right >> 1
        if left == right:
            print(left,right,count)
            break
    res = left<<count
    print(res)
    
solve(5,7)