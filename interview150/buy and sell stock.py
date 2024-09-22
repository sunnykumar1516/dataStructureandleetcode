#question number 121
def solve(prices):
    buy = prices[0]
    sell = prices[1]
    profit = 0
    for i in range(1,len(prices)):
        currentPrice = prices[i]
        buy = min(buy,prices[i-0])
        profit = max(profit,currentPrice-buy)
    print(profit)

a = [7,1,5,3,6,4]
#a = [7,6,4,3,1]
#a = [2,4,1]
solve(a)
    
    