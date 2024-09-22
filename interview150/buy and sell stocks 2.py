def solve(prices):
    length = len(prices)
    profit = 0
    buy = prices[0]
    sell = prices[1]
    profit = 0
    
    for i in range(1,length):
        cp = prices[i]
        if cp>prices[i-1]:
            profit = profit + cp-prices[i-1]
        
    