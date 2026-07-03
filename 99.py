def maxProfit(prices): #Best Time to Buy and Sell Stock II
    ans = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i - 1]
        if profit > 0:
            ans += profit
    return ans

# Example input
prices = [7, 1, 5, 3, 6, 4]

# Output
print(maxProfit(prices))