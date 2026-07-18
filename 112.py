from functools import lru_cache #Coin Change Top Down Recursive

def coinChange(coins, amount):
    @lru_cache(None)
    def dfs(rem):
        if rem == 0:
            return 0
        if rem < 0:
            return -1

        min_coins = float('inf')

        for c in coins:
            res = dfs(rem - c)
            if res != -1:
                min_coins = min(min_coins, 1 + res)

        return -1 if min_coins == float('inf') else min_coins

    return dfs(amount)

# Example Input
coins = [1, 2, 5]
amount = 11

# Output
print(coinChange(coins, amount))