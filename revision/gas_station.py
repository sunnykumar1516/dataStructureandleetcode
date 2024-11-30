def solve(gas , cost):
    if sum(gas)< sum(cost):
        return -1
    length = len(gas)
    total = 0
    res = 0
    for i in range(length):
        c = cost[i]
        g = gas[i]
        rem = g -c
        total = total + rem
        if total < 0:
            res = i+1
            total = 0
    print(res)
    
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
solve(gas,cost)
    