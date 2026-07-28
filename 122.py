def uniquePaths(m, n): #unique paths 
    dp = [[0] * n for _ in range(m)]

    # Fill the first column with 1
    for i in range(m):
        dp[i][0] = 1

    # Fill the first row with 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

# Example
m = 3
n = 7

result = uniquePaths(m, n)
print("Unique Paths:", result)