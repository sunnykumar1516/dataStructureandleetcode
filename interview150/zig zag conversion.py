def convert(s,k):
    
    mat = [[] for i in range(k)]
    i = 0
    goingup = False
    for item in s:
        mat[i].append(item)
        if goingup:
            i = i-1
        else:
            i = i+1
        if i == k-1:
            goingup = True
        if i == 0:
            goingup = False
    
    s = ''.join([ ''.join(row) for row in mat])
    print(s)
    print('--',mat)
convert("PAYPALISHIRING",3)