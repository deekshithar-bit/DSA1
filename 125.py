def minCost(n, cuts):# Min Cost to Cut a Stick (Rod Cutting Problem)
    dp = {}

    def dfs(start, end):
        if start >= end:
            return 0

        key = (start, end)
        if key in dp:
            return dp[key]

        min_cost = float('inf')

        for c in cuts:
            if start < c < end:
                curr_cost = (end - start) + dfs(start, c) + dfs(c, end)
                min_cost = min(min_cost, curr_cost)

        if min_cost == float('inf'):
            min_cost = 0

        dp[key] = min_cost
        return min_cost

    return dfs(0, n)


# Example
n = 7
cuts = [1, 3, 4, 5]

print("Minimum Cost:", minCost(n, cuts))