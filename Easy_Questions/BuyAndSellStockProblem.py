from typing import List

class Soluation:
    def maxProfit(self,prices: List[int]) -> int:
        l, r = 0, 1 # l = buy stock or R = sell stock
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        
        return maxP


obj  = Soluation()
Priceslist = [7,1,5,3,6,4]

result = obj.maxProfit(Priceslist)
print('result-> ',result)
# 5