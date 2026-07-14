from typing import List #Minimum Cost Climbing Stairs

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0, 0]
    for i in range(2, n + 1):
        dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
    return dp[n]

# Example input
cost = [10, 15, 20]

# Function call
result = minCostClimbingStairs(cost)

# Output
print(result)