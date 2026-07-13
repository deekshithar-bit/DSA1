def climbStairs(n): #Climbing Stairs 
    if n == 0:
        return 1

    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

# Example
n = 5
print("Number of ways:", climbStairs(n))