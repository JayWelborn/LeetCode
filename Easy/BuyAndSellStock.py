class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        profit = 0
        bought = False
        length = len(prices)
        buy_price = sys.maxsize
        if prices[0] <= prices[1]:
            buy_price = prices[0]
            bought = True
        
        for i in range(1, length - 1):
            if prices[i] > prices[i + 1] and bought:
                profit += prices[i] - buy_price
                bought = False
            if prices[i] < prices[i + 1] and not bought:
                buy_price = prices[i]
                bought = True
        
        if prices[-1] > buy_price and bought:
            profit += prices[-1] - buy_price
        
        return profit
