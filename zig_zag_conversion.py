#question number 6

def getZigZag(s,numRows):
    rows = [[] for row in range(numRows)]
    index = 0
    step = -1
    
    for char in s:
        rows[index].append(char)
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index = index+ step
    
    for i in range(numRows):
        rows[i] = ''.join(rows[i])
    return ''.join(rows)
        
            
        
s = "PAYPALISHIRING"
x =getZigZag(s,4)
print(x)