def change(amount, coins):#Coin Change 2
    n = len(coins)
    if n == 0:
        return 1 if amount == 0 else 0

    dp = [[-1] * n for _ in range(amount + 1)]

    def fn(rem, start):
        if rem == 0:
            return 1
        if rem < 0:
            return 0
        if dp[rem][start] != -1:
            return dp[rem][start]

        combinations = 0
        for i in range(start, n):
            combinations += fn(rem - coins[i], i)

        dp[rem][start] = combinations
        return combinations

    return fn(amount, 0)

# Example
amount = 5
coins = [1, 2, 5]

print(change(amount, coins))