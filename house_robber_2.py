
def rob(a):
    length = len(a)
    money = []
    money.append(a[0])
    money.append(max(a[0],a[1]))
    for i in range(length):
        s1 = a[i]+money[i-2]
        s2 = money[i-1]
        money.append(max(s1,s2))
    return money[length-1]
    
def robRound(a):
    length = len(a)
    a1 = a[1:]
    a2 = a[0:length-2]
    m1 = rob(a1)
    m2 = rob(a2)
    return max(m1,m2)
    
    
