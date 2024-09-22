def solve(prices):
    buy,sell,profit = prices[0],prices[1],0
    length = len(prices)
    for i in range(1,length):
        cp = prices[i]
        if cp>prices[i-1]:
            buy = min(buy,prices[i-1])
            p1 = cp-buy
            profit = max(profit,p1)
            if i+1<length-1:
                p2 = getprofit(i+1,length,prices)
                profit = max(profit,p1+p2)
    return profit
def getprofit(index,length,prices):
    profit = 0
    buy = prices[index]
    for i in range(index+1,length):
        cp = prices[i]
        if cp > prices[i - 1]:
            buy = min(buy, prices[i - 1])
            profit = max(profit,cp - buy)
        
    return profit

prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

#------------------------------2nd attempt
# using recursion

def solve2(prices):
    print("")
 
buy = True
profit = 0
def maxProfit(index,prices,buy,n,txn):
    
    profit = 0
    if index>=n:
        return 0
    if txn==0:
        #profit = max(profit)
        return profit
    print(profit)
    if(buy):
        # selling at i
        p1 = maxProfit(index+1,prices,False,n,txn-1) - prices[index]
        # not selling
        p2 = maxProfit(index+1,prices,True,n,txn)
        profit = max(profit,p1,p2)
    else:
       p3 = maxProfit(index+1,prices,False,n,txn)
       p4 = prices[index]+maxProfit(index+1,prices,True,n,txn-1)
       profit = max(profit,p3,p4)
    
    
    return profit
a = [1,2,3,4,5]
x = maxProfit(0,a,True,len(a),txn=4)
print(x)