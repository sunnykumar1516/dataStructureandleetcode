import math


def solve(coins , amount):
    coins.sort(reverse=True)
    
    def explore(temp,index,count):
        if temp==amount:
            return True,count
        if temp>amount:
            temp = temp - coins[index]
            index = index+1
            count = count-1
            if index+1>len(coins):return False,-1
        if temp<amount:
            c = temp+coins[index]
            return explore(c,index,count+1)
    status,count = explore(0,0,0)
    if status: return count
    return -1
#--------------------------
def solve2(coins, amount):
    #initialize
    res = [math.inf]*(amount+1)
    res[0]=0
    for i in range(1,amount+1):
        count =0
        for coin in coins:
            if coin <= i:
                prev = res[i-coin]+1
                cur = res[i]
                res[i]=min(prev,cur)
    print(res)
                
                
    

coins = [1,2,5]
amount = 11
#coins=[2]
#amount = 3

print(solve2(coins,amount))