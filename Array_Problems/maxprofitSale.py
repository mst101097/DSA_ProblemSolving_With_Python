# Stock Buy Sell to Maximize Profit
# Input: prices = [7,1,5,3,6,4]
# Output: 5

def maxProfitSale(price):
    n = len(price)
    cost = 0
    maxcost = 0 

    if n==0:
        return 0
    
    min_price = price[0]

    for i in range(n):

        min_price = min(min_price,prices[i])

        cost = prices[i]-min_price

        maxcost = max(maxcost,cost)
        
    return maxcost


prices = [7,1,5,3,6,4]
print(maxProfitSale(prices))