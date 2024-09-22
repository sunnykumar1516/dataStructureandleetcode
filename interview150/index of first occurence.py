
def findOccurence(hay,need):
    
    index = -1
    for i in range(len(hay)):
        for j in range(len(need)):
            item = need[j]
            if item == hay[i]:
                i = i+1
            else:
                break
                
            if j >= len(need)-1:
                index = i-j-1
                return index
    return index
hay = 'helhelolo'
need = 'helo'
x = findOccurence(hay,need)
print(x)