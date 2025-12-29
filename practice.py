class StockAnalyzer:
    def __init__(self, values):
        self.data = values

    def get_max_profit(self):
        lowest = self.data[0]
        best_profit = 0

        for rate in self.data:
            if rate < lowest:
                lowest = rate
            else:
                profit = rate - lowest
                if profit > best_profit:
                    best_profit = profit

        return best_profit

    def get_volatility(self):
        fluctuation_sum = 0

        for index in range(1, len(self.data)):
            fluctuation_sum += abs(self.data[index] - self.data[index - 1])

        return fluctuation_sum / (len(self.data) - 1)


# Input
prices_input = list(map(int, input().split()))

# Object creation
stock_obj = StockAnalyzer(prices_input)

# Output
print(f"Max Profit: {stock_obj.get_max_profit()}")
print(f"Volatility Index: {stock_obj.get_volatility():.2f}")
