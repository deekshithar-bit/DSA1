def superEggDrop(k, n): #Super Egg Drop
    dp = [0] * (k + 1)
    moves = 0

    while dp[k] < n:
        moves += 1
        for i in range(k, 0, -1):
            dp[i] = 1 + dp[i] + dp[i - 1]

    return moves


# Example usage
k = int(input("Enter number of eggs: "))
n = int(input("Enter number of floors: "))

result = superEggDrop(k, n)
print("Minimum number of moves required:", result)