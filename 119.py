def lengthOfLIS(arr): #Longest Increasing Subsequence
    n = len(arr)

    if n == 0:
        return 0

    dp = [1] * n
    lisLength = 1

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        lisLength = max(lisLength, dp[i])

    return lisLength


# Example
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", lengthOfLIS(arr))